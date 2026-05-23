from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
import re

BASE_DIR = Path(__file__).resolve().parent
INPUT_MD = BASE_DIR / "Prompt_Engineering_Showcase.md"
OUTPUT_PDF = BASE_DIR / "Prompt_Engineering_Showcase.pdf"


def clean_inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    return text


def build_pdf():
    md = INPUT_MD.read_text(encoding="utf-8")
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A4,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TitleCenter",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        leading=28,
        spaceAfter=18,
    ))
    styles.add(ParagraphStyle(
        name="Heading1Custom",
        parent=styles["Heading1"],
        fontSize=18,
        leading=22,
        spaceBefore=18,
        spaceAfter=10,
        textColor=colors.HexColor("#1f2937"),
    ))
    styles.add(ParagraphStyle(
        name="Heading2Custom",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        spaceBefore=14,
        spaceAfter=8,
        textColor=colors.HexColor("#374151"),
    ))
    styles.add(ParagraphStyle(
        name="Heading3Custom",
        parent=styles["Heading3"],
        fontSize=12,
        leading=15,
        spaceBefore=10,
        spaceAfter=5,
        textColor=colors.HexColor("#4b5563"),
    ))
    styles.add(ParagraphStyle(
        name="BodyCustom",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="BulletCustom",
        parent=styles["BodyText"],
        leftIndent=18,
        firstLineIndent=-10,
        fontSize=10,
        leading=14,
        spaceAfter=3,
    ))
    code_style = ParagraphStyle(
        name="CodeBlock",
        fontName="Courier",
        fontSize=8,
        leading=10,
        leftIndent=8,
        rightIndent=8,
        spaceBefore=4,
        spaceAfter=8,
        backColor=colors.HexColor("#f3f4f6"),
        borderPadding=6,
    )

    story = []
    in_code = False
    code_lines = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            code_text = "\n".join(code_lines).strip()
            story.append(Preformatted(code_text, code_style, maxLineLength=88))
            code_lines = []

    for raw_line in md.splitlines():
        line = raw_line.rstrip()
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                in_code = False
                flush_code()
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            story.append(Spacer(1, 4))
            continue
        if line.strip() == "---":
            story.append(Spacer(1, 10))
            continue
        if line.startswith("# "):
            text = clean_inline(line[2:].strip())
            if story:
                story.append(PageBreak())
            story.append(Paragraph(text, styles["TitleCenter"] if not story else styles["Heading1Custom"]))
        elif line.startswith("## "):
            story.append(Paragraph(clean_inline(line[3:].strip()), styles["Heading2Custom"]))
        elif line.startswith("### "):
            story.append(Paragraph(clean_inline(line[4:].strip()), styles["Heading3Custom"]))
        elif line.startswith("- "):
            story.append(Paragraph("- " + clean_inline(line[2:].strip()), styles["BulletCustom"]))
        elif re.match(r"^\d+\.\s", line):
            story.append(Paragraph(clean_inline(line), styles["BulletCustom"]))
        else:
            story.append(Paragraph(clean_inline(line), styles["BodyCustom"]))

    flush_code()
    doc.build(story)
    print(f"PDF generated: {OUTPUT_PDF}")


if __name__ == "__main__":
    build_pdf()
