#!/usr/bin/env python3
"""Generate JERA SCN deck anchored on EBITDA tree (knowledge/patterns/jera-scn-ebitda-tree.md)."""

import sys
from pathlib import Path

_scripts_dir = Path(__file__).resolve().parent
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.dml.color import RGBColor

from _config import output_paths

OUT_PATHS = output_paths("JERA_SCN_EBITDAツリー_v2.pptx")

IBM_BLUE = RGBColor(0x05, 0x3F, 0x87)
IBM_LIGHT = RGBColor(0xE8, 0xF0, 0xFA)
GRAY = RGBColor(0x5A, 0x5A, 0x5A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
TEXT = RGBColor(0x33, 0x33, 0x33)
ORANGE = RGBColor(0xC4, 0x50, 0x00)
ORANGE_BG = RGBColor(0xFF, 0xF3, 0xE0)
GREEN_BG = RGBColor(0xE8, 0xF5, 0xE9)
GREEN_LINE = RGBColor(0x2E, 0x7D, 0x32)
CAP_FILL = RGBColor(0xDE, 0xEB, 0xF7)
EN_FILL = RGBColor(0xF5, 0xF5, 0xF5)
FOOTER = "JERA｜SCN（EBITDAツリー基準）v2.1｜2026年8月13日"
FONT_BODY = 14
FONT_TITLE = 22
FONT_SUB = 12
FONT_FOOTER = 9
FONT_BOX = 12

# 有価証券報告書（第10期・2025年3月期）個別財務諸表 P.140–142（印字）
# 会計基準：JGAAP・親会社単体。連結IFRSセグメント（P.85）とは混在しない。
YUHO_FY25 = {
    "他社販売電力料": "3,752,519",
    "電気事業雑収益": "88,871",
    "燃料費": "2,887,113",
    "修繕費": "113,056",
    "消耗品費": "16,182",
    "委託費": "30,397",
    "賃借料": "5,091",
    "給料手当": "30,860",
    "厚生費": "5,932",
    "他社購入電力料": "235,909",
    "減価償却費_個別": "116,753",
    "減価償却費_連結参考": "199,593",
    "汽力発電費合計": "3,292,729",
    "電気事業営業利益_個別": "124,483",
    "セグメント利益_連結参考": "124,324",
    "一般管理費": "55,559",
    "接続供給託送料": "91,159",
    "事業税": "38,778",
    "その他未掲載合計": "185,496",
    "ガス供給収益": "421,320",
    "ガス供給費用": "415,958",
}
YUHO_SOURCE = "securities_report2506.pdf P.140–142（個別・印字）"
YUHO_SCOPE_NOTE = (
    "個別JGAAP・電気事業のみ｜ガス供給事業・一般管理費等185,496Mは対象外（抜粋）"
)


def set_bg(slide):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = WHITE


def add_section_title(slide, text):
    box = slide.shapes.add_textbox(Inches(0.32), Inches(0.18), Inches(12.70), Inches(0.55))
    tf = box.text_frame
    tf.text = text
    p = tf.paragraphs[0]
    p.font.size = Pt(FONT_TITLE)
    p.font.bold = True
    p.font.color.rgb = IBM_BLUE


def add_subtitle(slide, text, top=0.72):
    box = slide.shapes.add_textbox(Inches(0.32), Inches(top), Inches(12.70), Inches(0.40))
    tf = box.text_frame
    tf.word_wrap = True
    tf.text = text
    p = tf.paragraphs[0]
    p.font.size = Pt(FONT_SUB)
    p.font.color.rgb = GRAY


def add_footer(slide, section, num):
    f = slide.shapes.add_textbox(Inches(0.40), Inches(7.15), Inches(11.80), Inches(0.25))
    f.text_frame.text = f"{FOOTER}　｜　{section}"
    f.text_frame.paragraphs[0].font.size = Pt(FONT_FOOTER)
    f.text_frame.paragraphs[0].font.color.rgb = GRAY
    n = slide.shapes.add_textbox(Inches(12.55), Inches(7.15), Inches(0.45), Inches(0.25))
    n.text_frame.text = str(num)
    n.text_frame.paragraphs[0].font.size = Pt(FONT_FOOTER)
    n.text_frame.paragraphs[0].font.color.rgb = GRAY
    n.text_frame.paragraphs[0].alignment = PP_ALIGN.RIGHT


def style_cell(cell, font_size, header=False, center=False):
    cell.text_frame.word_wrap = True
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    cell.margin_left = cell.margin_right = Pt(3)
    cell.margin_top = cell.margin_bottom = Pt(2)
    for p in cell.text_frame.paragraphs:
        p.font.size = Pt(font_size)
        p.font.color.rgb = WHITE if header else TEXT
        p.font.bold = header
        if center:
            p.alignment = PP_ALIGN.CENTER
    if header:
        cell.fill.solid()
        cell.fill.fore_color.rgb = IBM_BLUE


def add_table(slide, data, left, top, width, height, font_size=FONT_BODY, col_widths=None, center_cols=None):
    rows, cols = len(data), len(data[0])
    ts = slide.shapes.add_table(rows, cols, left, top, width, height)
    table = ts.table
    center_cols = center_cols or set()
    if col_widths:
        for i, w in enumerate(col_widths):
            table.columns[i].width = w
    for r in range(rows):
        for c in range(cols):
            cell = table.cell(r, c)
            cell.text = data[r][c]
            style_cell(cell, font_size, header=(r == 0), center=(c in center_cols))
    return table


def new_slide(prs, title, subtitle=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    add_section_title(slide, title)
    if subtitle:
        add_subtitle(slide, subtitle)
    return slide


def add_box(slide, left, top, width, height, text, fill, line, font_size=FONT_BOX, bold=False):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.text = text
    p = tf.paragraphs[0]
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = TEXT
    p.alignment = PP_ALIGN.CENTER
    return shape


def add_oval(slide, left, top, width, height, text, fill, line, font_size=FONT_BOX, bold=True):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line
    shape.line.width = Pt(2 if bold else 1)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.text = text
    p = tf.paragraphs[0]
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = TEXT if fill != IBM_BLUE else WHITE
    p.alignment = PP_ALIGN.CENTER
    return shape


def connect(slide, x1, y1, x2, y2, color=GRAY):
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, x1, y1, x2, y2)
    line.line.color.rgb = color
    line.line.width = Pt(1.25)
    return line


def build_title(prs, n):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    t = slide.shapes.add_textbox(Inches(0.50), Inches(1.20), Inches(12.33), Inches(2.00))
    t.text_frame.text = "JERA Strategic Capability Network\nEBITDAツリー基準 SCN（v2.1・有報整合・個別JGAAP）"
    for p in t.text_frame.paragraphs:
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = IBM_BLUE
    s = slide.shapes.add_textbox(Inches(0.50), Inches(3.40), Inches(12.00), Inches(1.55))
    s.text_frame.word_wrap = True
    s.text_frame.text = (
        "McK 6/29 EBITDA分解 × 有価証券報告書（第10期・2025/3）個別財務諸表\n"
        f"出典：{YUHO_SOURCE}｜Value＝電気事業営業利益124,483M（ガス事業は対象外）\n"
        "knowledge/patterns/jera-scn-ebitda-tree.md v1.1"
    )
    s.text_frame.paragraphs[0].font.size = Pt(FONT_BODY)
    s.text_frame.paragraphs[0].font.color.rgb = GRAY
    add_footer(slide, "表紙", n)


def build_rationale(prs, n):
    slide = new_slide(
        prs,
        "SCN再設計のねらい",
        "施策マッピング・長嶋様→森崎様報告を同一フレーム（EBITDA→Capability→Enabler）で行う",
    )
    add_table(
        slide,
        [
            ["SCN層", "EBITDA基準での役割", "有報・管理会計との接続"],
            ["Value", "電気事業EBITDA最大化（Outcome KPI）\nDX/AIはValueに置かない", "電気事業営業利益124,483M（個別）＋D&A116,753M"],
            ["Capability", "EBITDA枝＝「～できる能力」\nMonitor KPI＝McK先行/遅行", "電気事業営業費用明細（汽力発電費＋他社購入電力料）"],
            ["Enabler", "AMP・DGD・Team DX・自立経営のKOPT束", "Process→Technologyの順（G7回避）"],
        ],
        Inches(0.30),
        Inches(1.15),
        Inches(12.70),
        Inches(2.55),
        col_widths=[Inches(1.35), Inches(7.35), Inches(4.00)],
    )
    note = add_box(
        slide,
        Inches(0.30),
        Inches(3.85),
        Inches(12.70),
        Inches(1.05),
        "報告3行：①Value＝有報のどの収益/費用枝か（個別JGAAP・＋/－明示）　"
        "②Capability＝Monitor KPI　③Enabler＝施策（行動→KPI→EBITDA枝）\n"
        "※1費目→複数Capabilityの重複紐づけあり（燃料費・人件費等）",
        ORANGE_BG,
        ORANGE,
        FONT_BODY,
        True,
    )
    add_footer(slide, "ねらい", n)


def build_yuho_mapping(prs, n):
    slide = new_slide(
        prs,
        "有報費目との対応（第10期・2025年3月期）",
        f"出典：{YUHO_SOURCE}（単位：百万円）｜{YUHO_SCOPE_NOTE}",
    )
    y = YUHO_FY25
    add_table(
        slide,
        [
            ["McK/SCNノード", "有報費目（汽力発電費＋他社購入電力料）", "符号", "FY25", "Capability"],
            ["送電量×スプレッド", "他社販売電力料", "＋", y["他社販売電力料"], "Cap-A"],
            ["付加収益", "電気事業雑収益", "＋", y["電気事業雑収益"], "Cap-A"],
            ["O&M・変動費（最大）", "燃料費（石炭・ガス・油等）", "－", y["燃料費"], "Cap-A2/B2*"],
            ["メンテナンス", "修繕費＋消耗品費", "－", f'{y["修繕費"]}＋{y["消耗品費"]}', "Cap-B1"],
            ["委託・賃借", "委託費＋賃借料", "－", f'{y["委託費"]}＋{y["賃借料"]}', "Cap-B3"],
            ["人件費", "給料手当＋厚生費", "－", f'{y["給料手当"]}＋{y["厚生費"]}', "Cap-B2/X2*"],
            ["他社電源", "他社購入電力料（汽力発電費と並列）", "－", y["他社購入電力料"], "Cap-A"],
            ["EBITDA加算", "減価償却費（個別・汽力発電費内）", "＋", y["減価償却費_個別"], "—"],
            ["Value-1", "電気事業営業利益（個別）", "＝", y["電気事業営業利益_個別"], "Value-1"],
            ["未掲載", "一般管理費＋接続供給託送料＋事業税", "－", y["その他未掲載合計"], "—"],
            ["対象外", "ガス供給事業（収益／費用）", "±", f'{y["ガス供給収益"]}/{y["ガス供給費用"]}', "—"],
        ],
        Inches(0.18),
        Inches(1.05),
        Inches(12.95),
        Inches(5.55),
        font_size=11,
        col_widths=[Inches(1.9), Inches(3.9), Inches(0.45), Inches(1.8), Inches(1.1)],
        center_cols={2},
    )
    add_box(
        slide,
        Inches(0.18),
        Inches(6.70),
        Inches(12.95),
        Inches(0.38),
        "*燃料費・人件費は複数Capabilityに重複紐づけ（排他分割ではない）",
        EN_FILL,
        GRAY,
        9,
    )
    add_footer(slide, "有報対応", n)


def build_ebitda_tree(prs, n):
    slide = new_slide(
        prs,
        "EBITDAツリー（有報費目整合・個別JGAAP）",
        f"McK 6/29構造 × {YUHO_SCOPE_NOTE}",
    )
    y = YUHO_FY25
    items = [
        (f"Value-1：電気事業営業利益（個別）\n{y['電気事業営業利益_個別']}M → EBITDA", "Outcome", IBM_BLUE, WHITE, 0.55, 1.02, 12.0, 0.62),
        (f"＋ 他社販売電力料 {y['他社販売電力料']}M\n＋ 雑収益 {y['電気事業雑収益']}M", "Cap-A 収益", IBM_LIGHT, IBM_BLUE, 0.55, 1.78, 12.0, 0.50),
        (f"－ 燃料費\n{y['燃料費']}M", "Cap-A2/B2*", CAP_FILL, IBM_BLUE, 0.55, 2.42, 3.85, 0.72),
        (f"－ 修繕費＋消耗品費\n{y['修繕費']}M＋{y['消耗品費']}M", "Cap-B1", CAP_FILL, IBM_BLUE, 4.55, 2.42, 3.85, 0.72),
        (f"－ 委託費＋賃借料\n{y['委託費']}M＋{y['賃借料']}M", "Cap-B3", CAP_FILL, IBM_BLUE, 8.55, 2.42, 3.95, 0.72),
        (f"－ 人件費\n{y['給料手当']}M＋{y['厚生費']}M", "Cap-B2/X2*", CAP_FILL, IBM_BLUE, 0.55, 3.28, 3.85, 0.72),
        (f"－ 他社購入電力料\n{y['他社購入電力料']}M", "Cap-A 費用", CAP_FILL, IBM_BLUE, 4.55, 3.28, 3.85, 0.72),
        (f"計画停止 MWh\n（管理会計・McK Cap-C1）", "Cap-C1", CAP_FILL, IBM_BLUE, 8.55, 3.28, 3.95, 0.72),
        (f"計画外停止 MWh\n（管理会計・McK Cap-C2/3）", "Cap-C2/3", CAP_FILL, IBM_BLUE, 0.55, 4.14, 7.85, 0.72),
        (f"＋ D&A {y['減価償却費_個別']}M\n（個別・EBITDA加算）", "P.140–142", EN_FILL, GRAY, 8.55, 4.14, 3.95, 0.72),
    ]
    for text, sub, fill, line, l, t, w, h in items:
        add_box(slide, Inches(l), Inches(t), Inches(w), Inches(h), f"{text}\n{sub}" if sub else text, fill, line, 11, fill == IBM_BLUE)
    add_box(
        slide,
        Inches(0.55),
        Inches(5.05),
        Inches(12.0),
        Inches(0.55),
        f"未掲載：一般管理費等 {y['その他未掲載合計']}M｜対象外：ガス供給 {y['ガス供給収益']}/{y['ガス供給費用']}M｜"
        f"参考：連結セグメント利益 {y['セグメント利益_連結参考']}M・D&A {y['減価償却費_連結参考']}M（P.85・混在禁止）",
        ORANGE_BG,
        ORANGE,
        9,
    )
    add_footer(slide, "EBITDAツリー", n)


def build_scn_map(prs, n):
    slide = new_slide(prs, "SCN全体像", "Value → Capability（主経路太線）→ Enabler束")
    add_oval(
        slide,
        Inches(4.60),
        Inches(0.95),
        Inches(4.20),
        Inches(0.70),
        "Value-1\n発電EBITDA最大化",
        IBM_BLUE,
        IBM_BLUE,
        10,
    )
    add_oval(
        slide,
        Inches(3.80),
        Inches(1.85),
        Inches(5.80),
        Inches(0.55),
        "Value-2：ユニット経済価値（NPV／複数年EBITDA）",
        IBM_LIGHT,
        IBM_BLUE,
        8,
        False,
    )
    add_box(
        slide,
        Inches(1.00),
        Inches(2.65),
        Inches(11.33),
        Inches(0.85),
        "【主経路・太線】C-0：発電所主体の収支PDCAを回せる能力\n"
        "Monitor：PDCA完遂・計画精度｜Enabler：AMP／原価管理PJ／Dataiku",
        ORANGE_BG,
        ORANGE,
        10,
        True,
    )
    caps = [
        ("Cap-A\n収益最大化", 0.55, 3.75),
        ("Cap-B\nO&M最適化", 3.55, 3.75),
        ("Cap-C1\n計画停止", 6.55, 3.75),
        ("Cap-C2/3\n計画外停止", 9.55, 3.75),
    ]
    for label, l, t in caps:
        add_oval(slide, Inches(l), Inches(t), Inches(2.85), Inches(0.95), label, CAP_FILL, IBM_BLUE, 9)
    enablers = [
        ("AMP構築PJ", 0.55),
        ("DGD/Team DX", 3.35),
        ("自立経営", 6.15),
        ("原価管理PJ", 8.95),
        ("McK DF（案）", 11.05),
    ]
    for label, l in enablers:
        add_box(slide, Inches(l), Inches(5.05), Inches(2.05), Inches(0.55), label, EN_FILL, GRAY, 8)
    # simple connectors
    cx = Inches(6.70)
    connect(slide, cx, Inches(1.65), cx, Inches(2.65))
    connect(slide, cx, Inches(3.50), cx, Inches(3.75))
    for l in [1.97, 4.97, 7.97, 10.97]:
        connect(slide, cx, Inches(3.50), Inches(l), Inches(3.75))
        connect(slide, Inches(l), Inches(4.70), Inches(l + 0.3), Inches(5.05))
    add_footer(slide, "SCN全体像", n)


def build_capability_table(prs, n):
    slide = new_slide(
        prs,
        "Capability一覧（EBITDA枝 × 主体列）",
        "○＝主担当　△＝支援／要確認",
    )
    headers = ["ID", "Capability", "有報/EBITDA枝", "所長", "本社", "DX", "Monitor KPI（例）"]
    rows = [
        ["C-0", "発電所主体の収支PDCAを回せる能力【太線】", "汽力発電費全体", "○", "○", "△", "PDCA完遂・計画精度"],
        ["C-A1", "需給・市場に応じた運転計画を実行できる", "他社販売電力料", "○", "△", "△", "稼働率・アベイラ"],
        ["C-A2", "熱効率・需給貢献で収益確保", "燃料費・雑収益", "○", "○", "○", "熱効率・起動回数"],
        ["C-B1", "保全・修繕を最適化", "修繕費・消耗品費", "○", "○", "○", "LCC・点検INT"],
        ["C-B2", "O&Mコスト（起動費等）管理", "燃料費（変動）・人件費", "○", "△", "△", "起動回数・FTE"],
        ["C-B3", "修繕・委託の生産性向上", "委託費・賃借料", "○", "○", "△", "修繕期間・委託単価"],
        ["C-C1", "計画停止を最適化", "計停MWh（管理会計）", "○", "○", "△", "計停日数"],
        ["C-C2", "計画外停止を防止", "計外MWh（管理会計）", "○", "○", "○", "計外率・バッドアクター"],
        ["C-C3", "計画外停止から早期復旧", "停止損失", "○", "△", "○", "復旧日数"],
        ["C-X1", "設備・収支・前提をtimely把握", "Input（全費目）", "○", "○", "○", "データ整備率"],
        ["C-X2", "標準プロセスで再現", "BPR・人件費効率", "○", "○", "△", "標準化・定着"],
        ["C-X3", "裁量で施策実行", "自立・ガバナンス", "○", "○", "—", "権限委譲"],
    ]
    add_table(
        slide,
        [headers] + rows,
        Inches(0.18),
        Inches(1.05),
        Inches(12.95),
        Inches(5.85),
        col_widths=[
            Inches(0.55),
            Inches(3.55),
            Inches(1.35),
            Inches(0.45),
            Inches(0.45),
            Inches(0.45),
            Inches(1.55),
        ],
        center_cols={3, 4, 5},
    )
    add_footer(slide, "Capability", n)


def build_enabler_table(prs, n):
    slide = new_slide(prs, "Enabler束・施策マッピング", "プログラム → Capability接続（重点領域）")
    add_table(
        slide,
        [
            ["Initiative束", "接続Cap", "KOPT要点", "主体"],
            ["AMP構築PJ", "C-0, C-C1–3", "P:収支PDCA To-Be / T:ユニット別収支 / O:責任分界", "AMP PJ（体制要確認）・長嶋SAP WG"],
            ["発電所自立経営", "C-0, C-X3", "O:10/1組織・権限 / P:所長PDCA", "運営統括・経営企画"],
            ["Team DX / DGD", "C-A–C, C-X1", "T:評点3+ / P:業務成熟度", "手川PM・長嶋PMO"],
            ["原価管理PJ", "C-0", "T:S4 Check / P:両輪PDCA / Dataiku(S4外)", "経営管理"],
            ["McK Digital Factory", "C-C1–3", "O+P:主管部深関与BPR", "国内運営+所長+DPP"],
        ],
        Inches(0.25),
        Inches(1.05),
        Inches(12.75),
        Inches(2.05),
        col_widths=[Inches(2.0), Inches(1.6), Inches(5.8), Inches(3.35)],
    )
    add_table(
        slide,
        [
            ["施策", "Cap", "有報/EBITDA枝", "所長", "本社", "DX"],
            ["AMP全体構築部会", "C-0", "汽力発電費全体", "○", "○", "△"],
            ["ユニット別収支DB", "C-0", "収支・燃料・修繕", "○", "○", "○"],
            ["計画外抑制部会", "C-C2", "計外MWh", "○", "○", "△"],
            ["設備保守DB部会", "C-C2,X1", "修繕費・消耗品費", "○", "○", "○"],
            ["J-AIME/G-DAC", "C-C2,A2", "計外・燃料効率", "△", "○", "○"],
            ["モデルプラントAI", "C-C2/B1", "要選定", "○", "○", "○"],
            ["業務棚卸(千葉)", "C-X2", "人件費・委託費", "○", "○", "△"],
            ["10/1組織変更", "C-X3,C-0", "全枝", "○", "○", "—"],
        ],
        Inches(0.25),
        Inches(3.25),
        Inches(12.75),
        Inches(3.55),
        col_widths=[Inches(2.4), Inches(1.1), Inches(1.8), Inches(0.5), Inches(0.5), Inches(0.5)],
        center_cols={3, 4, 5},
    )
    add_footer(slide, "Enabler", n)


def build_kpi_gap(prs, n):
    slide = new_slide(prs, "KPI配置とGap対応", "OutcomeはValue／MonitorはCapability／DX利用率はOutcomeにしない")
    add_table(
        slide,
        [
            ["レイヤ", "ノード", "指標種別", "例"],
            ["Value-1", "発電EBITDA", "Outcome", "電気事業営業利益124,483M＋D&A116,753M（個別）"],
            ["Value-2", "ユニット経済価値", "Outcome", "NPV・複数年EBITDA"],
            ["C-0", "収支PDCA", "Monitor", "PDCA完遂・計画精度"],
            ["C-B1", "修繕最適化", "Monitor", "修繕費・消耗品費（有報）"],
            ["C-A2", "燃料効率", "Monitor", "燃料費（有報最大費目）"],
            ["Enabler", "DX手段", "変革KPI", "導入スピード（EBITDA単独責任×）"],
        ],
        Inches(0.30),
        Inches(1.05),
        Inches(6.20),
        Inches(2.75),
    )
    add_table(
        slide,
        [
            ["Gap", "症状", "EBITDA SCNでの修正"],
            ["G1", "組織先行・中身後", "10/1権限とC-0 To-Beを同一図でExCom合意"],
            ["G2", "PDCA3系統分裂", "C-0にAMP/SAP/Dataikuを束ねOutcome一本化"],
            ["G3", "DGD体制未起動", "Team DX PMOをSCN右肩に明示"],
            ["G4", "地点未決", "C-Cに1拠点を太線"],
            ["G5", "KPI Open", "Value-1にストレッチ数値"],
            ["G6", "オーナー分散", "BPR→C-X2に集約"],
            ["G7", "DPP再演", "行動→KPI→EBITDA枝の連鎖必須"],
        ],
        Inches(6.70),
        Inches(1.05),
        Inches(6.30),
        Inches(3.55),
    )
    add_footer(slide, "KPI・Gap", n)


def main():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    n = 1
    build_title(prs, n)
    n += 1
    build_rationale(prs, n)
    n += 1
    build_yuho_mapping(prs, n)
    n += 1
    build_ebitda_tree(prs, n)
    n += 1
    build_scn_map(prs, n)
    n += 1
    build_capability_table(prs, n)
    n += 1
    build_enabler_table(prs, n)
    n += 1
    build_kpi_gap(prs, n)
    for path in OUT_PATHS:
        prs.save(str(path))
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
