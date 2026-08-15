#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate LinkedIn/Note source archives for Vol.001-015, sp01-sp09, erf01-erf03."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "knowledge" / "source" / "linkedin"


def write_en(folder: str, id_label: str, title: str, body: str) -> None:
    p = ROOT / folder / "en.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        f"# {id_label} — {title}\n\n## Source type\n\nLinkedIn English version\n\n## Original article\n\n{body.strip()}\n",
        encoding="utf-8",
    )


def write_ja(folder: str, id_label: str, title: str, body: str) -> None:
    p = ROOT / folder / "ja.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        f"# {id_label} — {title}\n\n## Source type\n\nnote日本語版\n\n## 原文\n\n{body.strip()}\n",
        encoding="utf-8",
    )


def write_metadata(folder: str, header: str, yaml_block: str, extra: str = "") -> None:
    p = ROOT / folder / "metadata.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    content = f"# Metadata — {header}\n\n```yaml\n{yaml_block.strip()}\n```\n"
    if extra:
        content += f"\n{extra.strip()}\n"
    p.write_text(content, encoding="utf-8")


def main() -> None:
    created: list[str] = []

    def track(path: Path) -> None:
        created.append(str(path.relative_to(ROOT.parent.parent.parent)))

    # --- 001 ---
    write_en(
        "001",
        "Vol.1",
        "Will AI replace human work? I don't think that's the right question.",
        """In infrastructure, utilities, and government, 
this question comes up all the time:

"Will AI replace human jobs?"

Honestly, in high-reliability environments, 
that's not what I see happening.

---

A better question might be:

What actually changes — and what doesn't — when AI is introduced?

---

From what I've seen, three things stand out:

1) A lot of execution work goes away 
Reporting, data processing, routine tasks — 
AI is simply better and faster here.

2) Decisions don't go away 
If anything, they become more visible. 
Because now you have better data — and fewer excuses.

3) Responsibility definitely doesn't go away 
When something goes wrong, 
no one turns to the algorithm.

They turn to people.

---

One way I tend to explain it:

・AI gives you a technically optimal answer 
・But people still decide what actually makes sense

---

For example, in power operations:

AI might say: 
"Shut this asset down within 7 days."

But the operator is thinking:

- Can we afford downtime right now? 
- What else is happening on the grid? 
- Have we seen this pattern before?

So the real decision becomes:

・ "Do we act now, or manage the risk differently?"

---

That part hasn't changed.

---

So no — people don't disappear.

What changes is the role.

From:
- doing the work 

To:
- making the call 

---

And in critical infrastructure,

that call still carries real responsibility.

---

This is Part 1 of a series on redefining human roles in the age of AI.""",
    )
    write_metadata(
        "001",
        "LinkedIn Vol.1",
        """id: "001"
title:
  en: "Will AI replace human work? I don't think that's the right question."
series:
  name: "Operational AI"
languages: [en]
status: migrated
tags:
  - operational-ai
  - human-roles
  - execution-vs-decision
  - critical-infrastructure""",
    )

    # --- 002 ---
    write_en(
        "002",
        "Vol.2",
        "What AI actually replaces (and what it doesn't)",
        """After the last post, I got a simple question:

"If AI doesn't replace decisions, 
then what exactly does it change?"

Here's how I usually think about it.

---

Most work in operations falls into three layers:

1) Execution 
The doing — processing, reporting, routine tasks 

2) Analysis 
Understanding — patterns, forecasts, optimization 

3) Decision 
Choosing — trade-offs, risk, accountability 

---

What I see happening is pretty straightforward:

・AI is taking over a lot of execution 
・It's getting very good at analysis 
・But decisions are still on us

---

Where things go wrong is when we try to automate the last part too early.

I've seen projects aiming to "automate decisions" 
before fixing execution or improving analysis.

That usually doesn't end well.

---

In practice (e.g., power operations):

- AI processes data automatically 
- AI suggests optimal scenarios 
- People decide what to actually do 

---

So it's not really AI vs human.

It's more like:

・work is being redistributed 

From:
- effort 

To:
- responsibility 

---

And that shift is bigger than it looks.

---

This is Part 2 of a series on redefining human roles in the age of AI.""",
    )
    write_metadata(
        "002",
        "LinkedIn Vol.2",
        """id: "002"
title:
  en: "What AI actually replaces (and what it doesn't)"
series:
  name: "Operational AI"
languages: [en]
status: migrated
tags:
  - operational-ai
  - execution
  - analysis
  - decision
  - work-redistribution""",
    )

    # --- 003 ---
    write_en(
        "003",
        "Vol.3",
        "The missing piece: context",
        """So if AI can analyze and optimize,

what's left for humans?

In one word:

context

---

AI is great at:
- processing data 
- spotting patterns 
- optimizing outcomes 

But decisions in real operations 
are rarely made on data alone.

---

There's always context:

- Can we stop this asset right now? 
- What else is happening in the system? 
- What are the consequences if we're wrong? 

---

A small example:

AI says: 
"Failure risk is high. Replace within 7 days."

But someone on the ground knows:

- demand is about to spike 
- backup is limited 
- similar issues lasted longer before 

So instead of following the recommendation blindly,

they adjust the approach.

---

That's not ignoring AI.

It's making sense of it.

---

That's what human judgment looks like in practice.

Not picking the best theoretical answer, 
but choosing what works in reality.

---

And that's harder than it sounds.

---

This is Part 3 of a series on redefining human roles in the age of AI.""",
    )
    write_metadata(
        "003",
        "LinkedIn Vol.3",
        """id: "003"
title:
  en: "The missing piece: context"
series:
  name: "Operational AI"
languages: [en]
status: migrated
tags:
  - operational-ai
  - context
  - human-judgment
  - operational-reality""",
    )

    # --- 004 ---
    write_en(
        "004",
        "Vol.4",
        "AI makes decisions easier… or does it?",
        """We often hear:

"AI makes work easier."

From what I've seen, 
that's only half true.

---

For execution, yes.

For decision-making, not really.

---

In fact, decisions often become harder.

---

Why?

Because AI removes effort, 
but leaves the responsibility.

---

Before AI:

You spend time gathering data, 
analyzing, discussing.

The process itself spreads the burden.

---

After AI:

The data is there instantly. 
The options are clear.

And now:

・you have to decide

---

There's nowhere to hide.

---

In real operations, this shows up like this:

AI gives you three solid options.

All of them make sense.

The question becomes:

・ "Which one are we willing to own?"

---

That's not easier.

That's heavier.

---

So AI doesn't eliminate complexity.

It just moves it.

From:
- execution 

To:
- decision-making 

---

And in critical systems,

that shift matters a lot.

---

This is Part 4 of a series on redefining human roles in the age of AI.""",
    )
    write_metadata(
        "004",
        "LinkedIn Vol.4",
        """id: "004"
title:
  en: "AI makes decisions easier… or does it?"
series:
  name: "Operational AI"
languages: [en]
status: migrated
tags:
  - operational-ai
  - decision-making
  - responsibility
  - complexity-shift""",
    )

    # --- 005 ---
    write_en(
        "005",
        "Vol.5",
        "So what kind of people matter in the age of AI?",
        """After talking about execution, analysis, and decision-making, 
a natural question comes up:

What kind of people are actually needed going forward?

---

From what I've seen, 
it's not about being "more technical" or "more strategic."

It's something else.

---

○The role is shifting

Not from "worker" to "executive."

But from:

- doing → deciding 
- following → interpreting 
- executing → owning 

---

○Three capabilities are becoming more important

1) Judgment under uncertainty 
Not everything is clear, even with perfect data. 
Someone still has to decide what to do.

---

2) Context awareness 
Understanding what's not in the data:
- operational constraints 
- real-world trade-offs 
- human factors 

---

3) Ownership 
Not just making decisions, 
but standing behind them.

---

○What's interesting is:

AI doesn't remove the need for people.

It removes the need for certain kinds of work.

---

Which means:

・The value of human work becomes more visible 

---

◯In critical infrastructure,

this becomes very clear.

Because decisions:
- have consequences 
- cannot be reversed easily 
- and must be explained 

---

◯So in the end:

It's not about humans vs AI.

It's about:

・Who is willing — and able — to take responsibility

---

That's what defines value going forward.

---

This is Part 5 (final) of a series on redefining human roles in the age of AI.""",
    )
    write_ja(
        "005",
        "Vol.5",
        "なぜAI時代ほど「人の専門性」が重要になるのか",
        """はじめに

AIが高度化するほど、人の専門性は不要になる。

そんな議論を耳にすることが増えた。

確かに、生成AIは既に、

* 要約
* 分析
* コード生成
* ドキュメント作成
* 情報検索

など、多くの知的作業を高速化し始めている。

しかし、少なくとも電力・交通・社会インフラのような"運用型産業"の世界では、少し違う景色も見え始めているように感じる。

むしろAI時代ほど、"人の専門性"が重要になっていく可能性がある。

AIが強い領域

まず前提として、AIは極めて強力だ。

特に、

* 大量データ処理
* パターン分析
* 異常検知
* 文章生成
* 構造化
* 横断検索

のような領域では、人間を大きく上回る場面も増えている。

例えば、数万件のログ分析や、複数システム横断での異常兆候探索などは、人間だけでは限界がある。

AIによって、これまで見えなかった相関や兆候が見えるようになる可能性は非常に大きい。

それでも残る「現実運用」

ただ、現実の運用環境は、必ずしも綺麗ではない。

そこには、

* undocumentedな構成
* 例外運用
* 暫定対応
* ベンダ依存
* 長年の運用慣習
* 現場特有の制約

が存在する。

そして、こうしたものは、単純なデータだけでは理解しきれない。

経験ある現場人材は、

「このアラームは普段と少し違う」

「この設備は数字以上に危ない」

「この操作は理論上問題なくても、現場では避ける」

といった、"数値化しにくい違和感"を持っている。

Human-in-the-loopの本質

最近、"Human-in-the-loop"という言葉をよく耳にする。

しかし、これは単なる"最終承認者"という意味ではない。

本来は、

* AIの提案
* 現場知識
* リスク判断
* 組織責任

を統合する役割だと思う。

AI時代になるほど、人は単純作業から解放される。

その代わり、

* 判断
* 責任
* 優先順位
* 例外処理
* 意味解釈

の重要性が増していく。

おわりに

これからの未来は、

「AIが人を置き換える世界」

というより、

「人の専門性とAIの役割分担を再設計する世界」

なのかもしれない。

特に社会インフラ領域では、この"協働設計"そのものが、競争力になっていくように感じている。""",
    )
    write_metadata(
        "005",
        "LinkedIn Vol.5",
        """id: "005"
title:
  en: "So what kind of people matter in the age of AI?"
  ja: "なぜAI時代ほど「人の専門性」が重要になるのか"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
tags:
  - operational-ai
  - human-expertise
  - judgment
  - ownership
  - human-in-the-loop""",
    )

    # --- 006 ---
    write_en(
        "006",
        "No.6",
        "Human expertise may become more important in the AI era — not less.",
        """One of the assumptions often discussed in the AI era is that human expertise will gradually become less important.
But in operational industries such as energy, utilities, transportation, and public infrastructure, I sometimes feel the opposite may also be true.
As AI becomes more capable, operational environments themselves become increasingly complex.
Organizations may soon operate environments where:
• AI-generated recommendations
• automated workflows
• operational agents
• predictive systems
• human decisions
all coexist simultaneously.
And in those moments, human expertise may become even more important — especially when dealing with ambiguity, exceptions, risk trade-offs, and operational accountability.
In real-world operations, not every situation can be fully standardized or modeled.
Experienced operators often understand:
• subtle operational anomalies
• field-specific risks
• historical context
• organizational constraints
• signals that are difficult to quantify
This type of tacit knowledge may become more valuable, not less, as AI adoption accelerates.
Perhaps the future is not simply:
"AI replacing humans."
But rather:
"Organizations redesigning how human expertise and AI work together."
In critical infrastructure, that balance may become one of the most important operational capabilities of all.""",
    )
    write_ja(
        "006",
        "No.6",
        "なぜOTの世界では「暗黙知」が消えないのか",
        """はじめに

DXやAIの議論では、

「属人化をなくす」

という言葉がよく使われる。

確かに、それ自体は重要だ。

しかし、OTの世界を見ていると、暗黙知は簡単には消えない。

むしろ、完全には消せないのではないかと思うこともある。

なぜ暗黙知が残るのか

OT環境は、

* 古い設備
* 長寿命資産
* 現場依存
* 例外運用
* 複雑な制約

が多い。

そのため、理論上正しい運用と、現実に安全な運用が一致しないことがある。

現場には「違和感知」がある

経験ある現場人材は、

* 音
* 振動
* 匂い
* 微妙な変化
* 過去トラブルの記憶

などから、異常兆候を感じ取る。

これは数値化しにくい。

AIと暗黙知

ただし、AIによって暗黙知の一部は"補助"できる可能性がある。

例えば、

* 作業記録
* 日報
* 障害履歴
* 会話ログ

などから、知識構造を整理することはできるかもしれない。

しかし最後は、人の経験と組み合わせる必要がある。

おわりに

重要なのは、暗黙知を「なくす」ことではなく、

「どう継承し、どうAIと共存させるか」

なのかもしれない。""",
    )
    write_metadata(
        "006",
        "LinkedIn No.6",
        """id: "006"
title:
  en: "Human expertise may become more important in the AI era — not less."
  ja: "なぜOTの世界では「暗黙知」が消えないのか"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
tags:
  - operational-ai
  - human-expertise
  - tacit-knowledge
  - ot
  - critical-infrastructure""",
    )

    # --- 007 ---
    og_en = """As AI adoption accelerates, governance is often discussed from a compliance perspective.

Policies.

Standards.

Risk controls.

Approval processes.

All of these are important.

But I increasingly believe they are not sufficient.

The real challenge is operational.

⸻

Many organizations still treat AI governance as a set of rules.

Something documented in a policy manual.

Something reviewed during audits.

Something owned by a governance committee.

The problem is that AI is no longer a static technology.

AI systems learn.

AI agents act.

Operational environments change.

Data changes.

Risks evolve.

Governance can no longer be something that exists outside operations.

It must become part of operations.

⸻

This is what I call Operational Governance.

Operational Governance is the ability to continuously align:

• AI decisions
• Human accountability
• Business objectives
• Operational reality

within day-to-day execution.

It is not merely about defining rules.

It is about ensuring those rules remain effective in practice.

⸻

Consider a critical infrastructure environment.

The question is not whether an AI model is accurate.

The question is whether the organization can:

• Detect failures
• Escalate exceptions
• Assign accountability
• Maintain auditability
• Adapt to changing conditions

These are operational capabilities.

Not technical features.

⸻

As AI becomes increasingly embedded into decision-making and execution, governance itself must evolve.

The future of governance is not bureaucracy.

It is operational capability.

And organizations that master Operational Governance may ultimately gain a greater advantage than those focused solely on AI capability itself."""

    write_en("007", "No.7", "What Is Operational Governance?", og_en)
    write_ja(
        "007",
        "No.7",
        "Operational AIとは何か",
        """はじめに

最近、"Operational AI"という言葉を意識することが増えている。

これは単なる生成AI活用とは少し違う。

Operational AIとは

個人的には、Operational AIとは、

「現実の運用環境の中で、安全・継続的に機能するAI」

だと考えている。

単に回答生成するだけではなく、

* 運用
* 統制
* 責任
* リスク
* Human-in-the-loop

を含めて成立するAI。

なぜ今重要なのか

AIは今後、

* 保全
* 障害対応
* リスク分析
* 顧客対応
* 制御支援

など、現場運用そのものへ入り始める。

そうなると、AIは"業務支援ツール"ではなく、"運用システム"に近づいていく。

Operational AIに必要なもの

Operational AIには、

* データ整備
* ログ
* トレーサビリティ
* ガバナンス
* 権限制御
* 現場知識

が必要になる。

つまり、AI単体では成立しない。

おわりに

今後の競争は、

「最も強いAI」

ではなく、

「最も現実運用に統合されたAI」

になるのかもしれない。

そしてその時、Operational AIは、企業の中核能力になっていくように感じている。""",
    )
    write_metadata(
        "007",
        "LinkedIn No.7",
        """id: "007"
title:
  en: "What Is Operational Governance?"
  ja: "Operational AIとは何か"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
patterns:
  - knowledge/patterns/operational-governance.md
tags:
  - operational-ai
  - operational-governance
  - ai-governance
  - critical-infrastructure""",
    )

    # --- 008 ---
    write_en(
        "008",
        "No.8",
        "Why Accountability Matters More in the Age of AI Agents",
        """The conversation around AI is rapidly shifting.

Not long ago, we were discussing how AI could generate content, summarize information, or improve productivity.

Today, the focus is increasingly on AI agents—systems capable of planning, reasoning, and executing tasks autonomously.

The promise is compelling.

AI agents can coordinate workflows, interact with systems, make recommendations, and increasingly take actions on behalf of humans.

But as autonomy increases, an important question emerges:

Who is accountable when an AI agent makes a mistake?

This is where many AI discussions become uncomfortable.

AI can generate decisions.
AI can execute actions.
AI can even recommend strategies.

Yet AI does not own consequences.

Organizations do.

In critical industries such as energy, finance, public services, and defense, this distinction becomes crucial.

An AI agent may recommend shutting down a system.

An AI agent may approve a transaction.

An AI agent may prioritize one operational response over another.

But when something goes wrong, accountability remains with people and institutions.

This is why I believe the future challenge of AI is not autonomy itself.

It is accountability architecture.

Organizations must define:

・What decisions AI can make
・What decisions humans must approve
・How accountability is assigned
・How actions are audited
・How exceptions are handled

The more autonomous AI becomes, the more important governance becomes.

Ironically, the age of AI agents may increase—not reduce—the importance of human responsibility.

AI can act as an agent.

But accountability will continue to belong to the principal.

That distinction may become one of the defining challenges of the AI era.""",
    )
    write_ja(
        "008",
        "No.8",
        "なぜAIエージェント時代ほど「責任」が重要になるのか",
        """生成AIの議論は急速に変化している。少し前までのテーマは、
	•	文章生成
	•	要約
	•	検索
	•	生産性向上だった。しかし今、関心はAIエージェントへ移りつつある。自律的に考え、計画し、実行するAI。その可能性は非常に大きい。一方で、自律性が高まるほど、避けて通れない問いがある。「誰が責任を持つのか」という問いだ。AIは提案できる。AIは判断できる。AIは実行できる。しかし、AIは結果に責任を持たない。責任を持つのは、組織であり、人である。この点は、電力・金融・公共・防衛といった重要インフラ領域では特に重要になる。AIエージェントが設備停止を提案するかもしれない。AIエージェントが業務優先順位を判断するかもしれない。AIエージェントが顧客対応を実行するかもしれない。しかし、結果として発生する影響やリスクを引き受けるのは人間だ。だからこそ、これから重要になるのはAIの自律性そのものではない。「責任構造の設計」である。どこまでAIに任せるのか。どこで人が介在するのか。誰が承認するのか。誰が説明責任を負うのか。どう監査するのか。AI時代の本質的な課題は、技術ではなく統制に移りつつある。AIエージェントはAgentになれる。しかしPrincipalにはなれない。この違いこそが、AI時代のガバナンスを考える上で最も重要な論点の一つなのだと思う。""",
    )
    write_metadata(
        "008",
        "LinkedIn No.8",
        """id: "008"
title:
  en: "Why Accountability Matters More in the Age of AI Agents"
  ja: "なぜAIエージェント時代ほど「責任」が重要になるのか"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
tags:
  - operational-ai
  - accountability
  - ai-agents
  - ai-governance
  - critical-infrastructure""",
    )

    # --- 010 ---
    write_en("010", "No.10", "What Is Operational Governance?", og_en)
    write_ja(
        "010",
        "No.10",
        "Operational Governanceとは何か",
        """AIガバナンスという言葉を聞くと、
多くの人は
	•	利用規程
	•	承認フロー
	•	リスク管理
	•	監査
を思い浮かべる。
もちろんそれらは重要だ。
しかし私は最近、
それだけでは不十分なのではないかと感じている。
本当の課題は、
ルールではなく運用にある。

多くの企業は、
AIガバナンスを
「守るべきルール」
として捉えている。
しかしAIはもはや静的なシステムではない。
モデルは更新される。
AIエージェントは行動する。
業務環境は変化する。
データも変化する。
リスクも変化する。
つまり、
ガバナンスを運用から切り離して考えることが難しくなっている。

私がOperational Governanceと呼んでいるものは、
AIと人間と業務と責任を、
日々の運用の中で継続的に整合させる能力である。
重要なのは、
ルールを作ることではない。
ルールが現実の運用の中で機能し続けることだ。

例えば重要インフラの世界では、
問題はAIの精度だけではない。
異常を検知できるか。
例外をエスカレーションできるか。
責任者を特定できるか。
監査可能か。
環境変化に対応できるか。
こうした能力が求められる。
これらは技術機能ではない。
運用能力である。

AIが意思決定や業務実行に深く入り込む時代、
ガバナンスもまた進化しなければならない。
未来のガバナンスは、
規程や統制だけではない。
運用能力そのものである。
そして私は、
AI活用能力よりも、
Operational Governance能力の方が、
長期的には大きな競争優位になるのではないかと考えている。""",
    )
    write_metadata(
        "010",
        "LinkedIn No.10",
        """id: "010"
title:
  en: "What Is Operational Governance?"
  ja: "Operational Governanceとは何か"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
patterns:
  - knowledge/patterns/operational-governance.md
tags:
  - operational-ai
  - operational-governance
  - ai-governance
  - critical-infrastructure""",
    )

    # --- 011 ---
    write_en(
        "011",
        "No.11",
        "Will AI Replace Experts, or Amplify Them?",
        """Will AI Replace Experts, or Amplify Them?
One of the most common questions in the AI era is:
Will AI eventually replace experts?
At first glance, the answer seems plausible.
AI can already summarize information, analyze data, generate content, and answer complex questions.
Many tasks that once required years of experience can now be completed in seconds.
But I believe this question is framed incorrectly.
The real question is not whether AI will replace experts.
It is whether organizations know how to combine AI and expertise effectively.

Expertise is often misunderstood.
People assume expertise is knowledge.
In reality, expertise is judgment.
It is the ability to interpret incomplete information, navigate ambiguity, and make decisions under uncertainty.
These capabilities are difficult to reduce to data alone.

This becomes especially visible in operational environments.
Experienced operators often recognize weak signals that never appear in manuals.
They understand context.
They understand consequences.
They understand exceptions.
AI can process information faster.
Experts often understand reality better.

The most successful organizations may not be those with the best AI.
They may be those that combine AI speed with human judgment.
AI expands access to knowledge.
Experts transform knowledge into decisions.

The future may not belong to AI alone.
Nor to experts alone.
It may belong to organizations that know how to amplify expertise through AI.""",
    )
    write_ja(
        "011",
        "No.11",
        "AIは専門家を代替するのか、それとも増幅するのか",
        """AIの進化によって、
「専門家は不要になるのではないか」
という議論をよく目にする。
確かにAIは驚異的なスピードで進化している。
検索し、
分析し、
要約し、
提案する。
これまで専門家が長い時間をかけて行っていた作業の一部は、確実にAIへ移行していくだろう。
しかし私は、
AIが専門家を代替するというより、
専門家を増幅する方向へ進むのではないかと考えている。

多くの人は、
専門性＝知識
だと思っている。
しかし実際には違う。
専門性とは、
不完全な情報の中で判断する能力であり、
曖昧さを扱う能力であり、
責任を持って意思決定する能力である。

特に電力やOTの世界では、
ベテランほど例外処理に強い。
異常の兆候を察知する。
状況の文脈を理解する。
判断結果の影響を理解する。
こうした能力は、単なる知識量だけでは説明できない。

AIは知識へのアクセスを民主化する。
しかし判断までは民主化しない。
だからこそ、
AI時代ほど専門家の役割は重要になる。
変わるのは、
知識提供者から、
判断者へと役割が移ることだ。

未来は、
AIか専門家か
ではない。
AIによって専門性をどう増幅するか
である。
そしてそれこそが、
Operational AI時代の競争力なのだと思う。""",
    )
    write_metadata(
        "011",
        "LinkedIn No.11",
        """id: "011"
title:
  en: "Will AI Replace Experts, or Amplify Them?"
  ja: "AIは専門家を代替するのか、それとも増幅するのか"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
patterns:
  - knowledge/patterns/expertise-amplification.md
tags:
  - operational-ai
  - expertise
  - human-judgment
  - amplification""",
    )

    # --- 012 ---
    write_en(
        "012",
        "No.12",
        "Competitive Advantage in the AI Era Will Come from Operating Models, Not Models",
        """Competitive Advantage in the AI Era Will Come from Operating Models, Not Models
Much of today's AI conversation focuses on models.
Which model is smartest?
Which benchmark is highest?
Which provider is leading?
These questions matter.
But they may matter less over time.

Models improve rapidly.
Capabilities spread quickly.
What is cutting-edge today often becomes widely available tomorrow.
Competitive advantage built solely on model access may be difficult to sustain.

What does not spread as quickly is organizational capability.
Operating models.
Governance structures.
Decision processes.
Human expertise.
Operational discipline.
These assets are far more difficult to replicate.

The organizations that gain the greatest value from AI may not be those with the best models.
They may be those with the strongest operating models around AI.
Organizations that know how to:
• Govern AI • Manage risk • Integrate human judgment • Handle exceptions • Continuously improve operations

In many industries, AI capability is becoming a commodity.
Operational capability is not.
The future competitive advantage may not come from AI itself.
It may come from the ability to operate AI effectively at scale.""",
    )
    write_ja(
        "012",
        "No.12",
        "AI時代の競争優位はモデルではなく運用体系から生まれる",
        """生成AIの議論では、
どのモデルが優れているのか
という話題が中心になりがちだ。
GPTなのか。
Claudeなのか。
Geminiなのか。
もちろん重要な論点である。
しかし私は、
長期的な競争優位はモデルそのものからは生まれないと考えている。

モデルは進化する。
性能差は縮まる。
優れた機能は急速に普及する。
つまり、
モデルそのものはコモディティ化していく可能性が高い。

一方で、
運用体系は簡単には真似できない。
組織文化。
意思決定構造。
ガバナンス。
専門家の知見。
現場理解。
改善サイクル。
こうしたものは、
一朝一夕には構築できない。

AI活用で成果を出す組織は、
最も優れたモデルを持つ組織ではない。
AIを最も上手く運用できる組織である。

AIを統制できるか。
リスクを管理できるか。
Human-in-the-Loopを設計できるか。
現実運用へ組み込めるか。
継続的に改善できるか。
こうした能力こそが差別化要因になる。

AI能力はコモディティ化する。
しかし運用能力はコモディティ化しない。
だから私は、
AI時代の競争優位は、
モデルではなく運用体系から生まれるのだと考えている。""",
    )
    write_metadata(
        "012",
        "LinkedIn No.12",
        """id: "012"
title:
  en: "Competitive Advantage in the AI Era Will Come from Operating Models, Not Models"
  ja: "AI時代の競争優位はモデルではなく運用体系から生まれる"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
patterns:
  - knowledge/patterns/operating-model-advantage.md
tags:
  - operational-ai
  - operating-model
  - commoditization
  - competitive-advantage""",
    )

    # --- 013 ---
    write_en(
        "013",
        "No.9",
        "Why Human-in-the-Loop Will Never Disappear",
        """As AI agents become increasingly capable, a common question emerges:

Will humans eventually be removed from decision-making?

I believe the opposite may be true.

The more autonomous AI becomes, the more important Human-in-the-Loop (HITL) becomes.

Many people view HITL as a safeguard until AI becomes reliable enough to operate independently.

I see it differently.

Human-in-the-Loop is not primarily about compensating for AI weaknesses.

It is about designing accountability.

AI can act as an agent.

But accountability remains with people and institutions.

This is especially true in industries such as energy, finance, public services, and defense.

The key question is not whether AI can make a decision.

The key question is who is legally, operationally, and ethically accountable for that decision.

For example, an AI system may recommend shutting down equipment or prioritizing maintenance activities.

Yet responsibility for safety, regulatory compliance, and operational continuity remains human.

As long as accountability remains human, Human-in-the-Loop remains necessary.

Not because AI is incapable.

But because responsibility cannot be delegated to technology.
Interestingly, enterprise AI platforms such as Palantir AIP already implement this concept.

AI generates recommendations, but a designated individual must approve actions before execution.

The goal is not merely to prevent mistakes.
It is to make accountability visible.

Who reviewed the recommendation?
Who approved the action?
Who owns the outcome?

In many ways, Human-in-the-Loop is becoming less of a technical safeguard and more of an accountability mechanism.

The future is not AI versus humans.
The future is AI with humans.

And in critical operational environments, Human-in-the-Loop may remain one of the most important design principles of Operational AI.""",
    )
    write_ja(
        "013",
        "No.9",
        "なぜHuman-in-the-Loopはなくならないのか",
        """AIエージェントの進化によって、
「人は意思決定のプロセスからいなくなるのか」
という議論を目にすることが増えた。
確かにAIは急速に進化している。
膨大な情報を分析し、提案し、計画し、そして実行する。
これまで人が担っていた業務の一部は、確実にAIへ移行していくだろう。
しかし私は、
AI時代になればなるほど、
Human-in-the-Loopの重要性は高まると考えている。

Human-in-the-Loopという言葉は、
「AIがまだ不完全だから人が監視する」
という意味で使われることが多い。
しかし本質はそこではない。
Human-in-the-Loopとは、
責任構造を設計するための仕組みである。
前回の記事でも触れたように、
AIはAgentにはなれる。
しかしPrincipalにはなれない。
AIは行動できるが、
結果に責任を持つことはできない。
責任を負うのは、
組織であり、
人である。
だからこそ、
重要な意思決定から人を完全に排除することは難しい。

特に重要インフラの世界では、
問題はAIが判断できるかどうかではない。
その判断に対して、
誰が法的責任や保安責任を負うのか
という点にある。
例えば電力業界では、
設備停止判断、
保守優先順位、
異常時対応などについて、
AIが有力な提案を行うようになるかもしれない。
しかし、
保安責任
法令遵守責任
説明責任
運用責任
は依然として人と組織に残る。
AIが事故や障害の責任を引き受けることはない。
責任を負うのは人である。
だからHuman-in-the-Loopは必要なのだ。
それはAIの性能不足によるものではない。
責任構造上の必然なのである。

興味深いことに、
この考え方はすでに実装され始めている。
例えばPalantir AIPのような企業向けAIプラットフォームでは、
AIが推奨を行い、
人が承認し、
その承認履歴を記録する
という仕組みが組み込まれている。
重要なのは、
その目的が単なるAIの暴走防止ではないことだ。
誰が判断したのか。
誰が承認したのか。
誰が結果に責任を持つのか。
それを明確にするための仕組みなのである。
言い換えれば、
Human-in-the-Loopは
「安全装置」
ではなく、
「責任装置」
なのかもしれない。

さらに現実の運用は、例外でできている。
設備異常。
災害対応。
想定外事象。
複数トラブルの同時発生。
情報不足の中での判断。
こうした状況では、
過去データだけでは解けない問題が数多く発生する。
AIは過去から学習する。
しかし運用は未来で起こる。
そして未来は、
必ずしも過去の延長線上には存在しない。
だからこそ、
最後の判断を担う人の存在が重要になる。

もちろん、
人の役割は変わっていく。
これからの人間は、
単純な作業者ではなく、
・判断者
・監督者
・リスク保有者
・例外対応者
としての役割を担うようになるだろう。
AIが仕事をする時代だからこそ、
人は「何をするか」ではなく、
「何に責任を持つか」が問われるようになる。

未来は、
AIか人間か
ではない。
AIと人間をどう共存させるか
である。
そしてその中心にあるのが、
Human-in-the-Loopなのだと思う。
AIがどれほど進化しても、
保安責任や法的責任が人に残る限り、
Human-in-the-Loopはなくならない。""",
    )
    write_metadata(
        "013",
        "LinkedIn No.13",
        """id: "013"
note_number: 9
title:
  en: "Human-in-the-Loop Is Not a Safety Mechanism—It's an Accountability Mechanism"
  ja: "Human-in-the-Loopは安全装置ではなく責任装置である"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
primary_framework:
  - frameworks/human-oversight.md
secondary_frameworks:
  - frameworks/decision-ownership.md
  - frameworks/ai-governability.md
patterns:
  - knowledge/patterns/decision-ownership.md
lessons:
  - knowledge/lessons/governance-messaging.md
tags:
  - ai-governance
  - operational-ai
  - human-in-the-loop
  - accountability
  - human-oversight
  - decision-ownership""",
        extra="""## Core Theme

Human-in-the-Loop should not be understood primarily as a temporary safety mechanism compensating for AI limitations.

Its more fundamental role is to preserve human and organizational accountability as AI systems gain greater operational autonomy.

## Relationship to No.14

No.13 establishes Human-in-the-Loop as an accountability mechanism.

No.14 extends this argument by separating Decision Execution from Decision Ownership.

## Relationship to No.16

No.16 reframes ownership as **risk ownership**: who holds risk after AI acts.

## Relationship to No.17

No.17 adds Capability vs Authority. Combined with No.13–14:

> Capability ↑ does not imply Authority ↑. Ownership, authority, and oversight must be designed together.""",
    )

    # --- 015 ---
    write_en(
        "015",
        "No.15",
        "Ownership Isn't Enough—It Must Be Verifiable",
        """Helping mission-critical organizations transform operations responsibly for the AI era

In enterprise AI, we've been discussing accountability.
Then we talked about decision ownership.
But I think there's another question that is becoming even more important:
How do you prove that ownership actually existed?
As AI agents become capable of making recommendations and executing workflows, simply recording who approved an action is no longer sufficient.
Organizations increasingly need to answer questions like:

	•	Who reviewed the recommendation?
	•	What information was available at the time?
	•	Which policy or authority governed the decision?
	•	Can an independent auditor verify all of this later?

These questions matter most in industries such as energy, finance, healthcare, and defense, where operational decisions carry legal, regulatory, or safety consequences.
Ownership without evidence eventually becomes trust based on assumption.
But operational trust cannot rely on assumptions.
It requires decisions that are verifiable, not merely documented.
Perhaps the future of AI governance is not about adding more approval steps.
It is about designing governance that remains transparent, auditable, and independently verifiable—even as AI becomes increasingly autonomous.
In the era of Operational AI, trust may ultimately depend not only on who owns a decision, but on whether that ownership itself can be proven.""",
    )
    write_ja(
        "015",
        "No.15",
        "責任者がいるだけでは足りない。「責任を証明できること」が重要になる",
        """AIガバナンスでは、「誰が責任を負うのか」という議論がよく行われます。
私自身もこれまで、
	•	Accountability（説明責任）
	•	Decision Ownership（意思決定の責任者）
について書いてきました。
しかし、AIエージェントが実際に業務を実行する時代になると、もう一つ重要な問いが生まれます。
「その責任は、本当に証明できるのか。」
たとえば、
AIが設備停止を提案し、人が承認したとします。
事故が起きた後、
「責任者は○○です。」
と言うだけでは十分ではありません。
本当に求められるのは、
	•	誰が確認したのか
	•	どの情報を見て判断したのか
	•	どのルールに従って承認したのか
	•	それを第三者が後から検証できるのか
ということです。
これは電力、防衛、金融、医療など、社会インフラを支える分野では特に重要になります。
責任は"存在する"だけでは意味がありません。
後から証明できて初めて、責任として成立します。
AIガバナンスも同じです。
ログを残すことが目的ではありません。
組織として、
「なぜその意思決定が行われたのか」
を後から説明できることが重要なのです。
Operational AIの時代に求められるのは、
AIを止めるためのガバナンスではなく、
AIと人間が行った意思決定を透明かつ検証可能な形で残す運用能力なのではないでしょうか。
私は、これからのAIガバナンスの競争力は、
「責任者がいること」ではなく、「責任を証明できること」に移っていくと考えています。""",
    )
    write_metadata(
        "015",
        "LinkedIn No.15",
        """id: "015"
title:
  en: "Ownership Isn't Enough—It Must Be Verifiable"
  ja: "責任者がいるだけでは足りない。「責任を証明できること」が重要になる"
series:
  name: "Operational AI"
languages: [en, ja]
status: migrated
patterns:
  - knowledge/patterns/verifiable-ownership.md
tags:
  - operational-ai
  - verifiable-ownership
  - auditability
  - ai-governance
  - critical-infrastructure""",
    )

    # --- SP01 ---
    write_en(
        "sp01",
        "SP01",
        "The conversation is shifting from AI productivity to AI resilience.",
        """Lately, it feels like the discussion around generative AI is starting to change quite rapidly.

Until recently, most conversations focused on copilots, automation, and productivity improvements.

But in critical infrastructure sectors such as finance, utilities, and the public sector, the priorities now seem to be shifting toward:

• AI-driven vulnerability detection 
• AI-assisted cyber defense 
• AI governance and control 
• Operational resilience with AI 

What I find particularly interesting is that some advanced AI capabilities are no longer being positioned for broad public release from day one.

Instead, access is increasingly being discussed in the context of governments, financial institutions, and large enterprises.

That suggests a subtle but important shift:

AI is beginning to be treated not only as a productivity tool, but also as a "critical resilience capability."

And that changes the conversation significantly.

The next challenge may not simply be:
"How do we use AI?"

But rather:
"How do we safely operate, govern, and integrate AI within critical environments?"

Especially in sectors where stability, trust, and continuity matter most, governance and operational design may become just as important as the model capability itself.""",
    )
    write_ja(
        "sp01",
        "SP01",
        "「AI Productivity」から「AI Resilience」へ",
        """はじめに

ここ数年、生成AIの議論は"生産性向上"が中心だった。

* Copilot
* 自動化
* 業務効率化
* 要約
* ドキュメント生成

など。

しかし最近、少し空気が変わり始めているように感じる。

なぜ今「レジリエンス」なのか

金融・電力・公共などの重要インフラ領域では、

* AIによる脆弱性分析
* AI支援型サイバー防御
* AI統制
* Operational Resilience

の重要性が急速に高まっている。

背景にあるのは、AIが"便利ツール"から、"インフラ能力"へ変わり始めていることだと思う。

Productivityだけでは足りない

重要インフラでは、

* 安定性
* 継続性
* 説明責任
* 安全性

が求められる。

そのため、単純な生産性向上だけでは不十分になる。

AI時代のレジリエンス

これから重要になるのは、

「AIをどう使うか」

だけではなく、

「AIをどう安全に統制しながら運用するか」

なのではないだろうか。

特に社会インフラでは、AIレジリエンスそのものが、新しい競争力になっていく可能性がある。""",
    )
    write_metadata(
        "sp01",
        "LinkedIn SP01",
        """id: "sp01"
title:
  en: "The conversation is shifting from AI productivity to AI resilience."
  ja: "「AI Productivity」から「AI Resilience」へ"
series:
  name: "Energy & AI Insights"
languages: [en, ja]
status: migrated
patterns:
  - knowledge/patterns/ai-resilience-shift.md
tags:
  - ai-resilience
  - productivity
  - critical-infrastructure
  - ai-governance""",
    )

    # --- SP02 ---
    write_en(
        "sp02",
        "SP02",
        "AI is changing the economics of cyber defense",
        """Recent discussions around advanced AI models being potentially used for cyberattacks against critical infrastructure are raising an important question:

What happens when vulnerability discovery itself becomes AI-scaled?

For years, cybersecurity in critical infrastructure has relied on layers of defense:

- perimeter security
- patch management
- SOC monitoring
- vendor governance
- operational procedures

But AI changes the economics of both attack and defense.

The issue is not simply that "AI can attack systems."
The deeper shift is that AI can dramatically accelerate the discovery of weaknesses across highly complex environments.

This is particularly significant for utilities, energy, transportation, and financial infrastructure, where organizations often operate with:

- legacy systems
- operational constraints
- systems that cannot easily be stopped
- highly interconnected environments
- tacit operational knowledge accumulated over decades

In that world, traditional human-centered security operations may struggle to scale fast enough.

What I find most interesting is that governments and enterprises are beginning to recognize another reality:

Defenders may also need AI to defend against AI.

This means AI adoption and AI resilience are becoming inseparable agendas.

The conversation is no longer only about "how to use AI."
It is increasingly about how to redesign operational models, governance, and infrastructure resilience for an AI-native era.

For critical infrastructure organizations, this may become one of the defining transformation themes of the next decade.""",
    )
    write_metadata(
        "sp02",
        "LinkedIn SP02",
        """id: "sp02"
title:
  en: "AI is changing the economics of cyber defense"
series:
  name: "Energy & AI Insights"
languages: [en]
status: migrated
tags:
  - cyber-defense
  - ai-resilience
  - critical-infrastructure
  - utilities""",
    )

    # --- SP03 ---
    write_en(
        "sp03",
        "SP03",
        "AI is not just improving utilities — it is redefining what they are.",
        """Recent developments in the Middle East, including tensions involving Iran, highlight how sensitive global energy systems remain to geopolitical factors.

	•	Around 20% of global oil flows through the Strait of Hormuz (IEA, EIA)
	•	LNG markets remain closely linked to geopolitical dynamics
	•	Japan's energy self-sufficiency is approximately 15% (METI)

These dynamics are not new. However, the operating environment for utilities is becoming increasingly complex:
• Greater price volatility • Higher penetration of renewables • More frequent extreme weather events • Growing electricity demand (including AI and data centers) • Structural workforce constraints
In this context, many discussions focus on how AI can improve operations.
That is certainly important — but it may not be sufficient.
👉 The shift we are seeing is broader: not just improving how things are done, but rethinking what needs to be done in the first place.
Utilities are evolving from: "providers of energy"
to: orchestrators of energy systems, assets, and customer interactions — in near real time
AI is not the objective. It is one of the key enablers of this transition.
What is changing includes:

	•	From periodic planning → more dynamic decision-making
	•	From siloed systems → more integrated IT/OT environments
	•	From manual execution → AI-supported operations
	•	From labor-intensive work → greater emphasis on human judgment and oversight

One observation:
Even without deliberate transformation, external conditions are already driving change.
Geopolitical developments, climate patterns, and demand shifts are gradually redefining operating assumptions.
So perhaps the key question is:
"What should utilities become in this evolving environment?"

#EnergyTransition #AI #Utilities #Geopolitics #DigitalTransformation

Sources (public):

	•	IEA (International Energy Agency)
	•	U.S. EIA (Energy Information Administration)
	•	METI (Japan Energy White Paper)
	•	IEA: Energy and AI""",
    )
    write_metadata(
        "sp03",
        "LinkedIn SP03",
        """id: "sp03"
title:
  en: "AI is not just improving utilities — it is redefining what they are."
series:
  name: "Energy & AI Insights"
languages: [en]
status: migrated
tags:
  - utilities
  - energy-transition
  - ai
  - geopolitics
  - digital-transformation""",
    )

    # --- SP04 ---
    write_en(
        "sp04",
        "SP04",
        "Liberalization shifted risk, not just power.",
        """Many expected deregulation to lower prices and foster innovation. But in reality, most new entrants struggled — or exited.
Why?
Because the playing field was never truly level.

	•	Incumbents own generation assets + long-term fuel contracts
	•	New entrants rely heavily on wholesale markets
	•	Price spikes (e.g., winter 2021) destroyed margins overnight

And unlike other industries, Without high-risk market-linked pricing, you can't easily pass costs to customers.
The result?
Liberalization shifted risk, not power.
This is not a failure of companies. It's a consequence of market design.
The real question is: Are we designing markets for competition — or for resilience?""",
    )
    write_metadata(
        "sp04",
        "LinkedIn SP04",
        """id: "sp04"
title:
  en: "Liberalization shifted risk, not just power."
series:
  name: "Energy & AI Insights"
languages: [en]
status: migrated
tags:
  - energy-markets
  - liberalization
  - risk
  - resilience""",
    )

    # --- SP05 ---
    write_en(
        "sp05",
        "SP05",
        "Renewables are not an energy problem. They are a grid problem.",
        """We often hear: "Just build more solar and wind."
But reality is more complex.

	•	Transmission capacity is limited
	•	Supply and demand don't align (the "duck curve")
	•	Renewable curtailment is increasing

We are literally throwing away clean energy.
Why?
Because electricitay is not just about generation. It's about delivery, timing, and control.
In other words: Electricity is not an energy business. It's a logistics system in real time.The grid is a warehouse with zero storage capacity.
If we don't redesign the grid, more renewables won't solve the problem — they will amplify it.""",
    )
    write_metadata(
        "sp05",
        "LinkedIn SP05",
        """id: "sp05"
title:
  en: "Renewables are not an energy problem. They are a grid problem."
series:
  name: "Energy & AI Insights"
languages: [en]
status: migrated
tags:
  - renewables
  - grid
  - energy-transition
  - duck-curve""",
    )

    # --- SP06 ---
    write_en(
        "sp06",
        "SP06",
        "Electricity markets are no longer one market. They are three.",
        """Most people think electricity is traded in a single market.
Not anymore.
Today, power systems operate across three layers:

	0.	Energy market (kWh) → buying electricity
	0.	Capacity market (kW) → securing future supply
	0.	Balancing market (Δ) → stabilizing the grid in real time

Why this complexity?
Because renewables changed everything.
We now need to pay for:

	•	Energy
	•	Availability
	•	Flexibility

Stability itself has become a commodity.
The implication is profound: Electricity is no longer just a product. It is a portfolio of services: Energy, Availability, and Flexibility.""",
    )
    write_metadata(
        "sp06",
        "LinkedIn SP06",
        """id: "sp06"
title:
  en: "Electricity markets are no longer one market. They are three."
series:
  name: "Energy & AI Insights"
languages: [en]
status: migrated
tags:
  - electricity-markets
  - energy
  - capacity-market
  - balancing-market""",
    )

    # --- SP07 ---
    write_en(
        "sp07",
        "SP07",
        '"Will AI surpass human intelligence?" That\'s the wrong question.',
        """"Will AI surpass human intelligence?"

That's the wrong question.

After reading today's article, one thing became clear:

✔️The real shift is not about AI replacing humans 
✔️It's about AI redefining how decisions are made

---

Before:
• Humans think 
• Data supports

Now:
• AI generates hypotheses at scale 
• Humans select and take accountability

---

The impact?

Not replacing top talent.

✔️Standardizing and elevating decision-making across the organization

Especially in infrastructure and regulated industries, where:
• Knowledge is tacit 
• Decisions are experience-driven 
• Processes are fragmented 

AI changes the game:

→ It externalizes knowledge 
→ It makes decision logic visible 
→ It enables repeatability at scale 

---

What we are seeing is a structural shift:

From organizations powered by individuals 
→ To organizations powered by decision systems

---

So the real question is not:
"Will AI outperform humans?"

It is:

👉 "Who (or what) will construct decisions going forward?\"""",
    )
    write_metadata(
        "sp07",
        "LinkedIn SP07",
        """id: "sp07"
title:
  en: "\"Will AI surpass human intelligence?\" That's the wrong question."
series:
  name: "Energy & AI Insights"
languages: [en]
status: migrated
tags:
  - decision-systems
  - ai
  - organizational-design
  - tacit-knowledge""",
    )

    # --- SP08 ---
    write_ja(
        "sp08",
        "SP08",
        "電力DXの本当の難しさは、AIではなくOperational Realityにある",
        """はじめに

電力DXというと、多くの場合、

* AI
* データ活用
* IoT
* 自動化

などが注目される。

しかし実際に現場に入ると、本当に難しいのは別のところにあるように感じる。

それは、"Operational Reality（現実運用）"だ。

現場は理想通りに動いていない

現実の電力運用環境には、

* レガシーシステム
* 個別最適
* 暗黙知
* 例外運用
* 暫定対応

が大量に存在する。

そして、それらによって現場はギリギリ成立している。

つまり、"綺麗に標準化された世界"ではない。

AI以前に必要なこと

AI活用を進める前に、多くの企業では、

* EAM
* 文書管理
* CMDB
* 業務標準化
* データ整備

が必要になる。

なぜなら、AIは"理解可能な構造"がなければ本来力を発揮しにくいからだ。

Operational Realityをどう扱うか

重要なのは、Operational Realityを否定しないことだと思う。

現場には、現場なりの合理性がある。

問題は、それをどう可視化し、統制し、AIと接続していくか。

ここに、今後の電力DXの本当の難しさがあるように感じている。""",
    )
    write_metadata(
        "sp08",
        "LinkedIn SP08",
        """id: "sp08"
title:
  ja: "電力DXの本当の難しさは、AIではなくOperational Realityにある"
series:
  name: "Operational AI (JP)"
languages: [ja]
status: migrated
patterns:
  - knowledge/patterns/operational-reality.md
tags:
  - operational-ai
  - operational-reality
  - power-dx
  - ot
  - legacy-systems""",
    )

    # --- SP09 ---
    write_ja(
        "sp09",
        "SP09",
        'AIガバナンスは"ルール"ではなく"運用能力"になる',
        """はじめに

AIガバナンスという言葉を聞くと、多くの人は、

* 利用ルール
* 社内規程
* コンプライアンス
* 承認フロー

をイメージするかもしれない。

もちろんそれらも重要だ。

しかし、電力や社会インフラのような"止められないシステム"を見ていると、AIガバナンスはもう少し実務的なものになっていくように感じる。

AIは運用の中に入っていく

これまでAIは、比較的"周辺業務"で使われることが多かった。

しかし今後は、

* 保全計画
* 障害対応
* 顧客対応
* 予兆検知
* リスク分析

など、運用そのものに入り始める。

そうなると、ガバナンスは単なる文書では成立しない。

Operational Governance

今後重要になるのは、"Operational Governance"だと思う。

つまり、AIを安全に運用するための実務能力。

例えば、

* ログ取得
* トレーサビリティ
* モデル監視
* 権限制御
* エスカレーション
* Human-in-the-loop

など。

これは単なるポリシーではなく、日々運用される仕組みである必要がある。

AI統制は「技術」だけではない

面白いのは、AIガバナンスは技術だけでは成立しない点だ。

* 組織
* 役割
* 意思決定
* 責任構造
* 運用設計

がセットになる。

つまりAIガバナンスとは、"経営・運用・技術"の接続そのものなのかもしれない。

おわりに

AI時代に重要なのは、単純に「AIを導入できるか」ではなく、

「AIを継続的かつ安全に運用できる組織を作れるか」

なのではないだろうか。""",
    )
    write_metadata(
        "sp09",
        "LinkedIn SP09",
        """id: "sp09"
title:
  ja: 'AIガバナンスは"ルール"ではなく"運用能力"になる'
series:
  name: "Operational AI (JP)"
languages: [ja]
status: migrated
patterns:
  - knowledge/patterns/operational-governance.md
tags:
  - operational-ai
  - operational-governance
  - ai-governance
  - critical-infrastructure""",
    )

    # --- ERF01 ---
    write_en(
        "erf01",
        "ERF01",
        "What should we expect from humans in an AI-first world? — Enterprise Redesign Framework Vol.1: Evaluation",
        """AI performing well on tests is not the real story. The real question is not evaluation—it's enterprise design.
Some time ago, there was discussion about AI achieving high performance on advanced exams.
But with some distance, what stands out more is this:
In an AI-first world, we are being forced to rethink how enterprises are designed.
This goes far beyond HR.
It impacts:

	•	Human–AI role allocation
	•	Process design
	•	Organizational structure and decision-making
	•	Skill definitions
	•	Culture
	•	Technology foundation

That said, I'll intentionally focus on one point today:
Evaluation.

Traditionally, we measured "how correctly someone can answer."
In an AI-first context, value shifts to:

	•	What questions are asked
	•	How decisions are made
	•	What responsibilities are taken

So the real question is not:
"Can humans outperform AI?"
But:
"In a world where AI is assumed, what do we expect from humans?"

This may look like an HR topic—but it's not.
Evaluation is the strongest signal of what an organization truly values.

AI is not the risk. Failing to redesign the enterprise is.

Next, I plan to share thoughts on human–AI role design.""",
    )
    write_metadata(
        "erf01",
        "Enterprise Redesign Framework Vol.1",
        """id: "erf01"
title:
  en: "What should we expect from humans in an AI-first world? — Enterprise Redesign Framework Vol.1: Evaluation"
series:
  name: "Enterprise Redesign Framework"
languages: [en]
status: migrated
tags:
  - enterprise-redesign
  - evaluation
  - human-ai-roles
  - organizational-design""",
    )

    # --- ERF02 ---
    write_en(
        "erf02",
        "ERF02",
        "How should we divide roles between humans and AI? — Enterprise Redesign Framework Vol.2: Role Design",
        """In my previous post, I discussed the redesign of evaluation.
Today, I want to focus on a more foundational question:
How should we design the roles between humans and AI?

A common misconception is that AI will simply replace human jobs.
What is actually happening is more structural:
Work itself is being decomposed and reassembled.

Here's how I frame the new role structure:

1️⃣ AI: Generation

	•	Information gathering & summarization
	•	Option generation
	•	Draft creation

👉 Speed and scale

2️⃣ Humans: Definition

	•	What problem to solve
	•	What questions to ask
	•	Setting assumptions and constraints

👉 Setting direction

3️⃣ Humans: Judgment

	•	Trade-offs
	•	Risk decisions
	•	Final accountability

👉 Owning outcomes

4️⃣ Humans + AI: Orchestration

	•	Integrating outputs
	•	Validating assumptions
	•	Translating into execution

👉 Turning insight into impact

The key point:
Humans do not need to compete with AI in the same domain.

The real competition is in:

	•	Quality of questions
	•	Quality of judgment
	•	Quality of orchestration

This is not just about task allocation.
It impacts:

	•	Organizational design
	•	Governance
	•	Skill models
	•	Evaluation systems (Vol.1)

So the real design question is:
Not "who does what," but "which layers should humans own."

In the AI era, competitive advantage will not come from people who can use AI.
It will come from organizations that can design work around AI.

Next: Process Re-architecture.""",
    )
    write_metadata(
        "erf02",
        "Enterprise Redesign Framework Vol.2",
        """id: "erf02"
title:
  en: "How should we divide roles between humans and AI? — Enterprise Redesign Framework Vol.2: Role Design"
series:
  name: "Enterprise Redesign Framework"
languages: [en]
status: migrated
tags:
  - enterprise-redesign
  - role-design
  - human-ai-roles
  - organizational-design""",
    )

    # --- ERF03 ---
    write_en(
        "erf03",
        "ERF03",
        "How should business processes be redesigned in an AI-first world? — Enterprise Redesign Framework Vol.3: Process Re-architecture",
        """In Vol.1, I discussed evaluation. In Vol.2, role design.
Today, I focus on the most practical question:
How do business processes change?

A common pattern I see in AI adoption is:

	•	Keep existing processes
	•	Add AI to optimize certain tasks

This does not lead to real transformation.

What is actually happening is not automation, but:
Process re-architecture.

Traditionally, processes were designed like this:
Before: Human-centered process

	0.	Information gathering
	0.	Analysis
	0.	Content creation
	0.	Review
	0.	Decision-making

👉 Sequential, human-driven

In an AI-first model, it shifts to:
After: AI-integrated process

	0.	Problem definition (Human)
	0.	Generation & analysis (AI)
	0.	Integration & validation (Human + AI)
	0.	Decision-making (Human)

👉 The center of gravity shifts

The key is not efficiency.
It is that:
Where value is created in the process fundamentally changes.

This leads to three redesign imperatives:

1️⃣ Repositioning steps

	•	Eliminating unnecessary intermediate work
	•	Increasing parallel processing
	•	Shifting review points

2️⃣ Redesigning decision points

	•	Defining where humans must intervene
	•	Establishing acceptance/rejection criteria for AI outputs

3️⃣ Elevating input design

	•	Prompts become design artifacts
	•	Assumptions and constraints define outcomes

As a result:
Work shifts from execution to design and judgment.

So the real question is:
Is your organization "using AI faster within existing processes," or "redesigning processes for an AI-first world"?

That difference will define performance in the near future.

In the AI era, competitive advantage will come not from tools, but from process design.

Next: Organization & Governance.""",
    )
    write_metadata(
        "erf03",
        "Enterprise Redesign Framework Vol.3",
        """id: "erf03"
title:
  en: "How should business processes be redesigned in an AI-first world? — Enterprise Redesign Framework Vol.3: Process Re-architecture"
series:
  name: "Enterprise Redesign Framework"
languages: [en]
status: migrated
tags:
  - enterprise-redesign
  - process-rearchitecture
  - ai-first
  - organizational-design""",
    )

    print(f"Generated source archives under {ROOT}")


if __name__ == "__main__":
    main()
