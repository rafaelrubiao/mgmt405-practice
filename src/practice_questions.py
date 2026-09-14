"""Student-facing practice questions for MGMT 405.
Each question is NEW (not copied from textbook/PSet/exam) but inspired by their conceptual structure.

Schema per question:
  id, module (key from MODULES), theme, format ('open' | 'mcq'),
  stem, ask, hints (list of 3 strings), solution (step-by-step text),
  --- open only ---
  answer (number), tolerance_abs (number), unit (str, e.g., '$' or '')
  --- mcq only ---
  choices (list of strings), correct_index (int)

MODULES — each entry is (key, module label, topic title, page slug).

Module NUMBERS follow "405 Module Numbers.docx". Module TITLES and the
Part I / Part II splits follow the Fall 2026 EMBA calendar, because that is the
document the links get pasted into, so the wording students read there should
match what they land on. The two sources agree on structure: eight modules, with
externalities inside Module 4 and auctions inside Module 8.

Each module builds to its own page (docs/<slug>.html) so the calendar can link
to a single week's material.
"""

MODULES = [
    ("M1",    "Module 1",           "Basic Concepts and Economic Principles",          "module-1"),
    ("M2",    "Module 2",           "Demand Analysis",                                 "module-2"),
    ("M3",    "Module 3",           "Production & Costs",                              "module-3"),
    ("M4-I",  "Module 4 (Part I)",  "Competitive Markets and Market Interventions",    "module-4-part-1"),
    ("M4-II", "Module 4 (Part II)", "Market Distortions / Externalities",              "module-4-part-2"),
    ("M5",    "Module 5",           "Monopoly and Monopolistic Competition",           "module-5"),
    ("M6",    "Module 6",           "Complex Pricing and Advanced Pricing Strategies", "module-6"),
    ("M7-I",  "Module 7 (Part I)",  "Oligopoly with Homogenous Goods",                 "module-7-part-1"),
    ("M7-II", "Module 7 (Part II)", "Oligopoly with Diff. Goods; Game Theory",         "module-7-part-2"),
    ("M8",    "Module 8",           "Auctions",                                        "module-8"),
]

QUESTIONS = []

# =================== MODULE 1: Basic Concepts ===================
QUESTIONS += [
{
    "id": "m1-q1", "module": "M1", "theme": "Opportunity Cost", "format": "open",
    "stem": "Tom currently works as a paralegal earning $60,000/year. He is considering a **3-year** law degree that costs $45,000/year in tuition plus $5,000/year in required books and materials. After graduating he expects to earn $115,000/year as a lawyer.",
    "ask": "What is Tom's total economic cost of completing the law degree (in dollars)?",
    "answer": 330000, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "Economic cost = EXPLICIT costs (out-of-pocket payments) + IMPLICIT costs (opportunity cost of resources used).",
        "Explicit costs are what he pays: tuition + books/materials, for each of the 3 years.",
        "The implicit cost is the salary he gives up by not working: $60,000 per year for 3 years. The future lawyer salary is NOT a cost; it only matters for whether the degree pays off (the economic profit from the degree), not for measuring the cost.",
    ],
    "solution": "Explicit cost = ($45,000 tuition + $5,000 materials) × 3 years = $150,000\nImplicit cost (foregone salary) = $60,000 × 3 years = $180,000\nTotal economic cost = $150,000 + $180,000 = $330,000\n\nThe future $115,000 salary is irrelevant to the COST: it affects whether the degree pays off (the economic profit from the degree), not the cost itself.",
},
{
    "id": "m1-q2", "module": "M1", "theme": "Sunk Cost and Economic Profit", "format": "open",
    "stem": "A pizzeria bought a commercial pizza oven two years ago for $24,000. They can sell it today on the used market for $9,000, or keep using it for one more year. Operating it one more year would generate $30,000 in revenue but cost $34,000 in dough, toppings, energy, and labor.",
    "ask": "What is the economic profit from selling the oven today rather than operating it for one more year?",
    "answer": 13000, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "Economic profit = accounting profit − opportunity cost. The $24,000 paid two years ago is SUNK; only what happens from today on matters.",
        "Accounting profit from selling today: +$9,000. The alternative you give up, operating one more year, is worth $30,000 − $34,000 = −$4,000. That −$4,000 is the opportunity cost of selling.",
        "Economic profit of selling = $9,000 − (−$4,000) = $13,000. Giving up a losing alternative makes selling look better, not worse.",
    ],
    "solution": "Sunk-cost rule: ignore the $24,000 paid two years ago.\n\nAccounting profit from selling today: +$9,000\nValue of the alternative given up (operate one more year): $30,000 − $34,000 = −$4,000\n\nEconomic profit = accounting profit − opportunity cost\n                = $9,000 − (−$4,000) = $13,000\n\nBecause the alternative loses money, the opportunity cost of selling is negative, so the economic profit is larger than the $9,000 cash received. Selling is the right decision.\n\nA common slip is to answer $9,000, forgetting that the alternative counts even when it is a loss.",
},
{
    "id": "m1-q3", "module": "M1", "theme": "Market Equilibrium", "format": "open",
    "stem": "The local market for artisanal honey has demand Q_d = 300 − 5P and supply Q_s = −60 + 7P, where Q is in jars/week and P is in dollars/jar.",
    "ask": "What is the equilibrium price P* (in dollars/jar)?",
    "answer": 30, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "At equilibrium, quantity demanded equals quantity supplied: Q_d = Q_s.",
        "Set 300 − 5P = −60 + 7P and solve for P.",
        "300 + 60 = 7P + 5P → 360 = 12P → P = 30.",
    ],
    "solution": "Set Q_d = Q_s:\n  300 − 5P = −60 + 7P\n  360 = 12P\n  P* = $30/jar\n\n(Equilibrium quantity: Q* = 300 − 5(30) = 150 jars/week. Check supply side: −60 + 7(30) = 150 ✓.)",
},
{
    "id": "m1-q4", "module": "M1", "theme": "Combined S/D Shifts", "format": "mcq",
    "stem": "A severe drought sharply reduces the wheat harvest (wheat is the key input for bread). At the same time, a popular low-carb diet trend sweeps the country, reducing consumers' appetite for bread.",
    "ask": "What happens to the equilibrium price and quantity of bread?",
    "choices": [
        "Price rises; quantity falls",
        "Price falls; quantity rises",
        "Price is ambiguous; quantity falls",
        "Price rises; quantity is ambiguous",
        "Both price and quantity are ambiguous",
    ],
    "correct_index": 2,
    "hints": [
        "Identify each shock and which curve it shifts: the drought is a SUPPLY shock (input cost); the diet trend is a DEMAND shock (taste).",
        "Drought reduces supply → S shifts LEFT (P up, Q down). Diet trend reduces demand → D shifts LEFT (P down, Q down).",
        "On quantity: both shifts push Q DOWN — unambiguous. On price: S-left pushes P up, D-left pushes P down — net depends on relative magnitudes → AMBIGUOUS.",
    ],
    "solution": "Supply shifts LEFT (wheat scarcity raises bread's cost). Demand shifts LEFT (low-carb taste change).\n\nQuantity: both shifts lower Q → Q falls UNAMBIGUOUSLY.\nPrice: supply-left raises P, demand-left lowers P → AMBIGUOUS (depends on which shift is larger).\n\nAnswer: Price is ambiguous; quantity falls.",
},
]

# =================== MODULE 2: Demand & Elasticity ===================
QUESTIONS += [
{
    "id": "m2-q1", "module": "M2", "theme": "Point Elasticity", "format": "open",
    "stem": "A boutique gym faces demand of Q = 5,000 − 100P memberships/year, where P is the monthly fee in dollars.",
    "ask": "What is the price elasticity of demand at P = $30?",
    "answer": -1.5, "tolerance_abs": 0.05, "unit": "",
    "hints": [
        "Point elasticity: e = (dQ/dP) · (P/Q).",
        "Compute Q at P=30: Q = 5,000 − 100·30 = 2,000. And dQ/dP = −100.",
        "e = (−100) · (30 / 2,000) = −3,000 / 2,000 = −1.5.",
    ],
    "solution": "Step 1 — Compute Q at the point: Q(30) = 5,000 − 100(30) = 2,000.\nStep 2 — Slope: dQ/dP = −100.\nStep 3 — Point elasticity:\n  e = (dQ/dP) · (P/Q) = (−100)(30/2,000) = −1.5\n\nSince |e| > 1, demand is ELASTIC at this price — the gym is in the region where raising the fee would reduce total revenue.",
},
{
    "id": "m2-q2", "module": "M2", "theme": "Elasticity from Two Points", "format": "open",
    "stem": "A bookstore sold 500 novels/month at $20 each. After raising the price to $22, monthly sales fell to 460 novels. Other conditions (season, competition, income) were unchanged.",
    "ask": "What is the implied price elasticity of demand?",
    "answer": -0.80, "tolerance_abs": 0.05, "unit": "",
    "hints": [
        "Use e = %ΔQ / %ΔP, with each percentage measured relative to the initial point.",
        "%ΔQ = (460 − 500)/500 = −0.08 = −8%. %ΔP = ($22 − $20)/$20 = +0.10 = +10%.",
        "e = (−8%) / (+10%) = −0.80.",
    ],
    "solution": "%ΔQ = (460 − 500) / 500 = −8%\n%ΔP = (22 − 20) / 20 = +10%\n\ne = (−8%) / (+10%) = −0.80\n\n|e| < 1, so demand is INELASTIC at this price — raising the price INCREASED total revenue (TR_old = $10,000; TR_new = $10,120).",
},
{
    "id": "m2-q3", "module": "M2", "theme": "Marginal Revenue", "format": "open",
    "stem": "Demand for a firm's product is Q = 300 − 2.5P, where P is the price in dollars.",
    "ask": "What is marginal revenue at Q = 50 (in dollars)?",
    "answer": 80, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "The MR rule applies to INVERSE demand (P as a function of Q), so rearrange the demand curve first.",
        "Solving Q = 300 − 2.5P for P gives P = 120 − 0.4Q. For P = a − bQ, marginal revenue is MR = a − 2bQ.",
        "So MR = 120 − 0.8Q. At Q = 50: MR = 120 − 0.8(50) = 120 − 40 = $80.",
    ],
    "solution": "Step 1 — Invert the demand curve:\n  Q = 300 − 2.5P  →  2.5P = 300 − Q  →  P = 120 − 0.4Q\n\nStep 2 — Total revenue: TR = P·Q = (120 − 0.4Q)·Q = 120Q − 0.4Q²\nStep 3 — Marginal revenue: MR = dTR/dQ = 120 − 0.8Q\n\nAt Q = 50: MR = 120 − 40 = $80.\n\n(Rule of thumb for linear demand: MR has the same intercept as inverse demand but TWICE the slope.)",
},
{
    "id": "m2-q4", "module": "M2", "theme": "Elasticity & Total Revenue", "format": "mcq",
    "stem": "A toll-road operator finds that demand for crossings is elastic at the current toll. The operator raises the toll by 5%.",
    "ask": "What is the most likely effect on the number of crossings and on toll revenue?",
    "choices": [
        "Crossings rise; revenue rises",
        "Crossings unchanged; revenue rises by exactly 5%",
        "Crossings fall; revenue unchanged",
        "Crossings fall less than 5%; revenue rises",
        "Crossings fall more than 5%; revenue falls",
    ],
    "correct_index": 4,
    "hints": [
        "Elastic demand means |e| > 1 — quantity reacts proportionally MORE than price.",
        "If the toll rises 5%, crossings fall by MORE than 5%.",
        "Since the quantity drop more than offsets the price increase, TR = P·Q falls.",
    ],
    "solution": "Elastic ⇒ |e| > 1 ⇒ |%ΔQ| > |%ΔP|.\n\nToll rises 5% → crossings fall more than 5% (in percentage terms). The quantity effect dominates → total revenue FALLS.\n\nIntuition: in the elastic region, a firm RAISES revenue by LOWERING price, not raising it.",
},
{
    "id": "m2-q5", "module": "M2", "theme": "Revenue-Maximizing Quantity", "format": "open",
    "stem": "A firm faces inverse demand P = 150 − 3Q.",
    "ask": "At what quantity is total revenue maximized?",
    "answer": 25, "tolerance_abs": 0, "unit": "",
    "hints": [
        "Total revenue is maximized where marginal revenue equals zero.",
        "MR for P = 150 − 3Q is MR = 150 − 6Q.",
        "Set 150 − 6Q = 0 → Q = 25.",
    ],
    "solution": "Inverse demand: P = 150 − 3Q\nMR = 150 − 6Q (twice the slope of demand)\n\nTR is max where MR = 0:\n  150 − 6Q = 0\n  Q* = 25\n\nAt Q = 25, P = 150 − 75 = $75 and TR = $1,875 (the maximum possible). This is also where demand is unit-elastic (|e| = 1).",
},
]

# =================== MODULE 3: Production & Costs ===================
QUESTIONS += [
{
    "id": "m3-q1", "module": "M3", "theme": "Bang-for-Buck Rule", "format": "mcq",
    "stem": "A factory's marginal product of labor is MP_L = 45 units/hour at a wage of $15/hour. Its marginal product of capital is MP_K = 90 units/hour at a rental rate of $36/hour.",
    "ask": "To produce the same output at lower cost, the factory should:",
    "choices": [
        "Hire more labor, less capital",
        "Hire more capital, less labor",
        "Keep the current input mix (already cost-minimizing)",
        "Hire more of both",
        "Hire less of both",
    ],
    "correct_index": 0,
    "hints": [
        "Cost-minimizing rule: MP_L / w = MP_K / p_K (equalize 'bang per buck').",
        "Compute the two ratios: MP_L/w = 45/15 = 3.0; MP_K/p_K = 90/36 = 2.5.",
        "Labor gives more output per dollar (3.0 > 2.5). Substitute toward labor: more L, less K. As L rises, MP_L falls (diminishing returns), and as K falls, MP_K rises — the ratios will equalize.",
    ],
    "solution": "Bang-for-buck ratios:\n  MP_L / w = 45 / $15 = 3.0 units per dollar\n  MP_K / p_K = 90 / $36 = 2.5 units per dollar\n\nLabor gives more output per dollar. To minimize cost at the same output, the factory should substitute toward LABOR — more L, less K. As L rises MP_L falls, and as K falls MP_K rises, until the two ratios equalize.",
},
{
    "id": "m3-q2", "module": "M3", "theme": "Average Total Cost", "format": "open",
    "stem": "A small print shop has the following total cost schedule (Q = books printed/day, TC in dollars):\n  Q=0: TC=1,500\n  Q=10: TC=2,100\n  Q=20: TC=2,500\n  Q=30: TC=3,000\n  Q=40: TC=3,800\n  Q=50: TC=5,000",
    "ask": "What is the average total cost (ATC) at Q = 40?",
    "answer": 95.00, "tolerance_abs": 0.05, "unit": "$",
    "hints": [
        "ATC = TC / Q. Read TC at Q=40 from the table.",
        "TC at Q=40 is $3,800.",
        "ATC = $3,800 / 40 = $95.00.",
    ],
    "solution": "ATC = TC / Q\n     = $3,800 / 40\n     = $95.00 per book\n\n(For comparison: AFC = $1,500/40 = $37.50; AVC = $2,300/40 = $57.50; ATC = $95.00. AFC + AVC = ATC ✓.)",
},
{
    "id": "m3-q3", "module": "M3", "theme": "Marginal Cost from Quadratic TC", "format": "open",
    "stem": "A firm's total cost function is TC(Q) = 80 + 6Q + 0.25Q².",
    "ask": "What is the marginal cost at Q = 12 (in dollars)?",
    "answer": 12, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "MC = dTC/dQ. Take the derivative of the cost function.",
        "TC = 80 + 6Q + 0.25Q² → MC(Q) = 6 + 0.5Q.",
        "At Q = 12: MC = 6 + 0.5(12) = 6 + 6 = $12.",
    ],
    "solution": "TC(Q) = 80 + 6Q + 0.25Q²\nMC(Q) = dTC/dQ = 6 + 0.5Q\n\nAt Q = 12:  MC = 6 + 0.5(12) = $12.\n\n(Note: the fixed cost $80 doesn't appear in MC — that's why FC never affects the profit-maximizing output level.)",
},
{
    "id": "m3-q4", "module": "M3", "theme": "Shutdown Rule", "format": "open",
    "stem": "A small candle-maker operates in a perfectly competitive market. Its total cost is TC = 800 + 6Q + 0.2Q², and the market price is $18 per candle.",
    "ask": "Compute the firm's profit at the profit-maximizing quantity (in dollars; enter a negative number if it's a loss).",
    "answer": -620, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "For a price-taker, profit-max is where P = MC. Find MC and solve.",
        "MC = 6 + 0.4Q. Set MC = 18: 0.4Q = 12 → Q* = 30.",
        "TR = $18 × 30 = $540. TC = 800 + 6(30) + 0.2(30²) = 800 + 180 + 180 = $1,160. Profit = 540 − 1,160 = −$620. Check AVC = 6 + 0.2Q = 6 + 6 = $12 at Q=30 → P=$18 > AVC=$12, so the firm SHOULD keep operating in the short run (losing $620 beats shutting down and losing the full fixed cost of $800).",
    ],
    "solution": "Step 1 — Profit-max: P = MC.\n  MC = 6 + 0.4Q. Set = 18: Q* = 30.\nStep 2 — Compute revenue and cost:\n  TR = 18·30 = $540\n  TC = 800 + 6(30) + 0.2(30²) = 800 + 180 + 180 = $1,160\nStep 3 — Profit:\n  π = $540 − $1,160 = −$620\n\nShould the firm operate? Check AVC at Q=30: VC = 6(30) + 0.2(900) = 360, so AVC = $12. Since P=$18 > AVC=$12, the firm covers its variable costs and contributes toward the fixed $800. Operating: loss = $620. Shutting down: loss = $800. → OPERATE.",
},
{
    "id": "m3-q5", "module": "M3", "theme": "Marginal Cost of Equal-Pay Hire", "format": "open",
    "stem": "A custom furniture workshop employs 4 carpenters, each paid $180/day. To handle a backlog, the workshop wants to hire a 5th carpenter, who has agreed to join at $230/day. However, internal policy requires all carpenters to be paid the same wage.",
    "ask": "What is the marginal cost (per day) of hiring the 5th carpenter? (In dollars.)",
    "answer": 430, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "If equal pay must hold, all 5 carpenters must be paid the new (higher) rate.",
        "Before: 4 × $180 = $720/day. After: 5 × $230 = $1,150/day.",
        "Marginal cost of the 5th carpenter = $1,150 − $720 = $430.",
    ],
    "solution": "Before hire: total wage bill = 4 × $180 = $720.\nAfter hire (everyone at $230): 5 × $230 = $1,150.\n\nMarginal cost = $1,150 − $720 = $430.\n\nThis is much more than the new carpenter's own salary of $230 — the extra $200 reflects the raise the workshop must give the existing 4 carpenters ($50 × 4). A classic example of how labor-market constraints raise the true marginal cost of hiring.",
},
{
    "id": "m3-q6", "module": "M3", "theme": "Marginal Analysis (Hiring)", "format": "open",
    "stem": "A car wash currently serves 80 cars/day at $15 each. The owner is considering hiring another attendant at $90/day. With the extra attendant, throughput would rise to 95 cars/day, but to attract the additional volume the owner would lower the price to $14.",
    "ask": "What is the change in total revenue from hiring the extra attendant (new TR − old TR, in $)? Use this to check whether the wage is worth paying.",
    "answer": 130, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "TR = price × quantity. Compute TR before and after the hire.",
        "Before: 80 × $15 = $1,200. After: 95 × $14 = $1,330.",
        "Change in TR = $1,330 − $1,200 = $130. Since $130 > $90 wage, hiring is worthwhile.",
    ],
    "solution": "TR_before = 80 × $15 = $1,200\nTR_after = 95 × $14 = $1,330\nΔTR = $1,330 − $1,200 = $130\n\nThe marginal revenue from the extra attendant ($130) exceeds the wage ($90), so the owner should hire. Net gain = $130 − $90 = $40/day.",
},
]

# =================== MODULE 4-I: Perfect Competition ===================
QUESTIONS += [
{
    "id": "m4i-q1", "module": "M4-I", "theme": "Long-Run PC Equilibrium", "format": "open",
    "stem": "In a perfectly competitive market for organic milk, every firm has identical long-run cost curves with LATC minimized at Q = 50 gallons/day and a minimum LATC of $6/gallon. Market demand is Q_d = 6,000 − 300P (where Q is in gallons/day and P in $/gallon).",
    "ask": "In long-run equilibrium, how many firms operate in this market?",
    "answer": 84, "tolerance_abs": 0, "unit": "",
    "hints": [
        "Long-run PC equilibrium: each firm earns zero economic profit, so P = min LATC.",
        "P* = $6. Compute total market quantity at this price: Q_market = 6,000 − 300(6) = 4,200.",
        "Each firm produces 50 gallons at min LATC. Number of firms = 4,200 / 50 = 84.",
    ],
    "solution": "Long-run zero-profit condition: P = min LATC = $6.\n\nMarket Q at P=$6:\n  Q_market = 6,000 − 300(6) = 4,200 gallons/day\n\nEach firm produces Q_i = 50 gallons (the cost-minimizing scale).\n\nNumber of firms = 4,200 / 50 = 84.\n\n(Sanity check: each firm earns zero economic profit because P = min LATC.)",
},
{
    "id": "m4i-q2", "module": "M4-I", "theme": "Short-Run Operating Decision", "format": "mcq",
    "stem": "A perfectly competitive firm faces market price P = $22. At its profit-maximizing output level it has ATC = $26, AVC = $19, and MC = $22.",
    "ask": "In the short run, the firm should:",
    "choices": [
        "Exit the industry immediately",
        "Increase output until ATC = P",
        "Shut down — ATC exceeds price",
        "Operate — price covers AVC",
        "Operate and earn positive profit",
    ],
    "correct_index": 3,
    "hints": [
        "Short-run shutdown rule: operate if P ≥ AVC, shut down if P < AVC.",
        "Here P = $22 ≥ AVC = $19, so the firm should OPERATE in the short run.",
        "P < ATC ($22 < $26) means the firm is making negative economic profit, but by operating it covers VC and contributes $3/unit toward fixed costs. Shutting down means a loss equal to the full fixed cost — a worse outcome.",
    ],
    "solution": "Compare P to AVC, not ATC.\n  P = $22, AVC = $19 → P > AVC → OPERATE.\n  P = $22, ATC = $26 → P < ATC → losing money.\n\nBy operating, the firm covers all variable costs and earns $3/unit toward fixed costs. Shutting down would mean a loss equal to total fixed cost. Operating is the lesser loss.",
},
{
    "id": "m4i-q3", "module": "M4-I", "theme": "PC Firm Profit", "format": "open",
    "stem": "A perfectly competitive widget producer has TC = 600 + 5Q + 0.05Q². The market price is P = $9/widget.",
    "ask": "What is the firm's profit at the profit-maximizing quantity (in $; negative for loss)?",
    "answer": -520, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "Profit-max for a price-taker: P = MC. Solve for Q.",
        "MC = 5 + 0.1Q. Set = 9: Q* = 40.",
        "TR = 9(40) = $360. TC = 600 + 5(40) + 0.05(40²) = 600 + 200 + 80 = $880. Profit = $360 − $880 = −$520. (AVC at Q=40 is 5 + 0.05·40 = $7 < P, so the firm still operates in the SR.)",
    ],
    "solution": "MC = 5 + 0.1Q. Set P = MC:\n  9 = 5 + 0.1Q → Q* = 40.\n\nTR = 9 × 40 = $360\nTC = 600 + 5(40) + 0.05(40²) = 600 + 200 + 80 = $880\nProfit = $360 − $880 = −$520\n\nShould the firm operate? AVC at Q=40: VC = 5(40) + 0.05(40²) = 280, so AVC = $7. P=$9 > AVC=$7 → operate. The −$520 loss beats shutting down (loss of FC = $600).",
},
{
    "id": "m4i-q4", "module": "M4-I", "theme": "PC Producer Surplus", "format": "open",
    "stem": "In a perfectly competitive market, the supply curve is Q_s = 5P − 25 (where Q is in units and P in $). The market price is P = $20.",
    "ask": "What is the total producer surplus (in $)?",
    "answer": 562.5, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "Producer surplus = area between the market price and the supply curve, from Q = 0 to the equilibrium Q.",
        "At P = $20: Q = 5(20) − 25 = 75 units. Supply choke price (price at which Q = 0): 0 = 5P − 25 → P = $5.",
        "PS is the triangle: ½ × base × height = ½ × Q × (P − P_choke) = ½ × 75 × ($20 − $5) = $562.50.",
    ],
    "solution": "Step 1 — Find Q at P=$20: Q = 5(20) − 25 = 75.\nStep 2 — Find the supply-side price intercept (where Q=0): 5P − 25 = 0 → P = $5.\nStep 3 — PS is the triangle bounded by:\n  • P = $20 (top)\n  • the supply curve (rising from $5 at Q=0 to $20 at Q=75)\n  • the y-axis\n\n  PS = ½ × 75 × ($20 − $5) = ½ × 75 × 15 = $562.50.",
},
]

# =================== MODULE 4-II: Distortions & Externalities ===================
QUESTIONS += [
{
    "id": "m4ii-q1", "module": "M4-II", "theme": "Tax — Buyer Price", "format": "open",
    "stem": "A market has demand Q_d = 120 − 3P and supply Q_s = −30 + 2P. The government imposes a $5/unit tax on sellers.",
    "ask": "What is the new equilibrium price PAID BY BUYERS (in $)?",
    "answer": 32, "tolerance_abs": 0.1, "unit": "$",
    "hints": [
        "First find the free-market equilibrium. With a tax on sellers, P_buyer = P_seller + tax.",
        "Free-market: 120 − 3P = −30 + 2P → P* = 30.  With the tax: substitute P_seller = P_buyer − 5 into supply: Q_s = −30 + 2(P_b − 5) = −40 + 2P_b. Equate to demand.",
        "120 − 3P_b = −40 + 2P_b → 160 = 5P_b → P_b = $32.",
    ],
    "solution": "Step 1 — Free-market equilibrium:\n  120 − 3P = −30 + 2P → 150 = 5P → P* = $30, Q* = 30.\n\nStep 2 — With $5 tax on sellers, P_buyer = P_seller + 5, so supply (in terms of the buyer's price) shifts up. New supply: Q_s = −30 + 2(P_b − 5) = −40 + 2P_b.\n\nStep 3 — New equilibrium:\n  120 − 3P_b = −40 + 2P_b\n  160 = 5P_b\n  P_buyer = $32\n\nSeller receives $32 − $5 = $27. Quantity falls from 30 to Q = 120 − 3(32) = 24.",
},
{
    "id": "m4ii-q2", "module": "M4-II", "theme": "Tax Incidence", "format": "open",
    "stem": "Continuing the previous problem (Q_d = 120 − 3P, Q_s = −30 + 2P, $5 tax on sellers).",
    "ask": "Of the $5 tax, what fraction is borne by buyers? (Express as a decimal — e.g., 0.40.)",
    "answer": 0.40, "tolerance_abs": 0.02, "unit": "",
    "hints": [
        "Buyer's burden = how much the buyer's price ROSE from the original equilibrium.",
        "P_buyer rose from $30 to $32 → buyers pay $2 more out of the $5 tax.",
        "Buyer's share = $2 / $5 = 0.40. (Sellers absorb $3, or 60%.)",
    ],
    "solution": "Old buyer price: $30.  New buyer price: $32.  Increase = $2.\nTax = $5. Buyer's share = $2 / $5 = 0.40.\n\n(Demand slope = −3, supply slope = +2. The MORE-INELASTIC side bears MORE of the tax. Supply is less elastic here (2 < 3) → sellers bear more, 60%.)",
},
{
    "id": "m4ii-q3", "module": "M4-II", "theme": "Price Ceiling DWL", "format": "open",
    "stem": "A market has demand Q_d = 240 − 4P and supply Q_s = 6P. The government imposes a price ceiling at P_ceiling = $18.",
    "ask": "What is the deadweight loss caused by the price ceiling (in $)?",
    "answer": 270, "tolerance_abs": 2, "unit": "$",
    "hints": [
        "First find the free-market equilibrium. Then determine quantities at the ceiling and the DWL triangle.",
        "Free-market: 240 − 4P = 6P → P* = $24, Q* = 144. At ceiling P=$18: Q_s = 108 (only this much is supplied — the binding constraint), Q_d = 168 (demanders want more). Q_traded = 108.",
        "DWL triangle: ½ × (Q_eq − Q_traded) × (P_demand at Q_traded − P_supply at Q_traded). At Q=108: P_demand = (240−108)/4 = $33; P_supply = 108/6 = $18. DWL = ½ × (144−108) × ($33 − $18) = ½ × 36 × 15 = $270.",
    ],
    "solution": "Step 1 — Free-market equilibrium:\n  240 − 4P = 6P → 240 = 10P → P* = $24, Q* = 144.\n\nStep 2 — At the ceiling P = $18:\n  Q_s = 6(18) = 108 (supplied — binding constraint)\n  Q_d = 240 − 4(18) = 168 (wanted)\n  Q_traded = 108 (the SHORT side rules)\n\nStep 3 — DWL triangle, bounded by:\n  • the demand curve (top side)\n  • the supply curve (bottom side)\n  • from Q = 108 up to Q* = 144\n\n  At Q = 108: P_demand = $33, P_supply = $18.\n  DWL = ½ × (Q* − Q_traded) × (P_d − P_s) = ½ × 36 × 15 = $270.",
},
{
    "id": "m4ii-q4", "module": "M4-II", "theme": "Pigouvian Tax", "format": "mcq",
    "stem": "A chemical plant has a private marginal cost of $3.00/unit. Producing each unit emits pollution that imposes an estimated $0.80/unit external cost on society.",
    "ask": "What per-unit Pigouvian tax is needed to internalize the externality and achieve the socially efficient quantity?",
    "choices": [
        "$3.80/unit",
        "$2.20/unit",
        "It depends on demand elasticity",
        "Zero — markets handle externalities efficiently on their own",
        "$0.80/unit",
    ],
    "correct_index": 4,
    "hints": [
        "A Pigouvian tax should equal the EXTERNAL marginal cost at the socially-optimal quantity.",
        "External MC here is $0.80/unit — the cost the polluter doesn't pay but society bears.",
        "Set tax = $0.80, so the firm's effective cost becomes $3.00 + $0.80 = $3.80 = social MC.",
    ],
    "solution": "Pigouvian tax = external marginal cost.\n\nHere external MC = $0.80/unit. A tax of $0.80/unit internalizes the externality: producers face $3.00 (private MC) + $0.80 (tax) = $3.80 = social MC. The market then equilibrates at the socially efficient quantity.\n\n(Answer: $0.80/unit)",
},
{
    "id": "m4ii-q5", "module": "M4-II", "theme": "Consumer Surplus", "format": "open",
    "stem": "Linear demand for fresh-squeezed juice at a stand is P = 12 − 0.3Q (Q in cups/day). The stand sells juice at P = $6.",
    "ask": "What is the consumer surplus (in $)?",
    "answer": 60, "tolerance_abs": 0.5, "unit": "$",
    "hints": [
        "CS is the triangle between the demand curve and the price line, from 0 to the quantity sold.",
        "At P = $6: Q = (12 − 6)/0.3 = 20 cups. Price intercept of demand (price at Q = 0) = $12.",
        "CS = ½ × Q × (P_intercept − P) = ½ × 20 × ($12 − $6) = $60.",
    ],
    "solution": "Step 1 — Quantity sold at P=$6:\n  6 = 12 − 0.3Q → 0.3Q = 6 → Q = 20.\nStep 2 — Demand's price intercept (price at Q=0): $12.\nStep 3 — CS = ½ × base × height\n        = ½ × 20 × ($12 − $6)\n        = $60.",
},
]

# =================== MODULE 5: Monopoly & Mon Comp ===================
QUESTIONS += [
{
    "id": "m5-q1", "module": "M5", "theme": "Monopoly Profit-Max Price", "format": "open",
    "stem": "A monopolist sells a patented gadget. Inverse demand is P = 50 − Q (where Q is units/day and P is $/unit). Marginal cost is constant at $10.",
    "ask": "What is the profit-maximizing price (in $)?",
    "answer": 30, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "Monopoly profit-max: MR = MC. Find MR, set equal to MC, solve for Q, then read P off the demand curve.",
        "MR = 50 − 2Q (twice the slope of P = 50 − Q). Set MR = MC: 50 − 2Q = 10 → Q* = 20.",
        "Plug Q* = 20 into demand: P* = 50 − 20 = $30.",
    ],
    "solution": "Step 1 — MR from linear demand: MR = 50 − 2Q.\nStep 2 — Set MR = MC: 50 − 2Q = 10 → Q* = 20.\nStep 3 — Read P from demand: P* = 50 − 20 = $30.\n\n(Profit per unit = P − MC = $20. Total profit (assuming no FC) = $20 × 20 = $400.)",
},
{
    "id": "m5-q2", "module": "M5", "theme": "Monopoly Deadweight Loss", "format": "open",
    "stem": "The same monopolist (P = 50 − Q, MC = $10) sells at the profit-maximizing price.",
    "ask": "What is the deadweight loss of monopoly (in $)?",
    "answer": 200, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "DWL = the triangle between the demand curve and MC, from Q_monopoly to Q_competitive. Area = ½ × (Q_PC − Q_M) × (P_M − MC).",
        "Q_competitive (where P = MC): 50 − Q = 10 → Q_PC = 40. Q_monopoly = 20 (from the previous question). P_monopoly = $30, MC = $10.",
        "DWL = ½ × (40 − 20) × ($30 − $10) = ½ × 20 × 20 = $200.",
    ],
    "solution": "Step 1 — PC quantity (where P = MC): 50 − Q = 10 → Q_PC = 40.\nStep 2 — Monopoly quantity (from M5.Q1): Q_M = 20; P_M = $30.\nStep 3 — DWL is the triangle between demand and MC, from Q_M to Q_PC:\n          DWL = ½ × (Q_PC − Q_M) × (P_M − MC)\n              = ½ × (40 − 20) × ($30 − $10)\n              = ½ × 20 × 20\n              = $200.",
},
{
    "id": "m5-q3", "module": "M5", "theme": "Lerner Index", "format": "open",
    "stem": "A monopolist sells at P = $60 with constant MC = $24.",
    "ask": "What is the Lerner index? (As a decimal, e.g., 0.40.)",
    "answer": 0.60, "tolerance_abs": 0.01, "unit": "",
    "hints": [
        "Lerner index measures market power: L = (P − MC) / P.",
        "Plug in: L = ($60 − $24) / $60.",
        "L = $36 / $60 = 0.60 (60% of the price is markup over MC).",
    ],
    "solution": "Lerner index: L = (P − MC) / P = (60 − 24) / 60 = 36/60 = 0.60.\n\nThis equals 1/|e_D| at the profit-maximizing point, so the implied demand elasticity is |e_D| = 1/0.60 ≈ 1.67.",
},
{
    "id": "m5-q4", "module": "M5", "theme": "FC Effect on Monopolist", "format": "mcq",
    "stem": "A monopolist faces a new annual government licensing fee (a fixed cost). Its marginal cost is unchanged.",
    "ask": "In the short run, what happens to the monopolist's profit-maximizing price?",
    "choices": [
        "Price rises to pass the new cost on to consumers",
        "Price falls because total cost rises",
        "Price is unchanged — only profit changes",
        "Price rises by exactly the new fixed cost",
        "The monopolist always shuts down when a fixed cost rises",
    ],
    "correct_index": 2,
    "hints": [
        "Profit-max comes from MR = MC. A fixed cost doesn't appear in MC.",
        "If MC is unchanged, the optimal Q and P are unchanged.",
        "Only PROFIT (level) changes — it falls by the licensing fee. (As long as the firm still earns enough to cover variable costs, it keeps the same P and Q.)",
    ],
    "solution": "Profit-max condition: MR = MC. A fixed cost doesn't enter MC, so the optimal Q (and hence P) is UNCHANGED.\n\nWhat changes: profit falls by exactly the licensing fee.\n\nThis is why a one-time fee, license, or property-tax change doesn't get passed through to consumers in the short run — even a monopolist can't profit from raising P above the MR = MC level.",
},
{
    "id": "m5-q5", "module": "M5", "theme": "Monopolistic Competition LR Profit", "format": "open",
    "stem": "In a monopolistically competitive industry (many firms with differentiated products, free entry), a typical firm in long-run equilibrium has P = $25, Q = 60, ATC = $25, MC = $16.",
    "ask": "What is the typical firm's long-run economic profit (in $)?",
    "answer": 0, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "Long-run economic profit in monopolistic competition: free entry drives profit to zero.",
        "Profit = (P − ATC) × Q. With P = $25 and ATC = $25, what does that give?",
        "Profit = (25 − 25) × 60 = $0. P = ATC always in LR mon comp.",
    ],
    "solution": "Long-run mon comp equilibrium: P = ATC (free entry erodes any positive profit).\n\nProfit = (P − ATC) × Q = ($25 − $25) × 60 = $0.\n\nNotice P = $25 > MC = $16, so there's still a markup (Lerner = (25−16)/25 = 36%). But because the firm operates above min ATC (excess capacity), all that markup just covers average fixed cost — no economic profit.",
},
]

# =================== MODULE 6: Pricing Strategies ===================
QUESTIONS += [
{
    "id": "m6-q1", "module": "M6", "theme": "Two-Part Tariff", "format": "open",
    "stem": "A tennis club faces typical-member demand Q = 24 − 0.4P, where Q is court-hours/month and P is the per-hour price. The club's marginal cost per court-hour is $5. The club charges a TWO-PART TARIFF (monthly fee + per-hour price).",
    "ask": "What is the profit-maximizing MONTHLY FEE (in $)?",
    "answer": 605, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "Optimal two-part tariff with identical customers: per-unit price = MC, fee = consumer surplus at that price.",
        "Set per-hour P = MC = $5. Compute Q at this price: Q = 24 − 0.4(5) = 22. The price-axis intercept of inverse demand: from Q = 24 − 0.4P, P = 60 − 2.5Q, so at Q=0, P = $60.",
        "CS = ½ × Q × (P_intercept − price) = ½ × 22 × ($60 − $5) = ½ × 22 × 55 = $605. That's the maximum fee.",
    ],
    "solution": "Two-part tariff rule for homogeneous customers:\n  Per-unit price = MC (here, $5)\n  Membership fee = consumer surplus at that price\n\nStep 1 — Q at P = MC = $5:\n  Q = 24 − 0.4(5) = 22 court-hours.\nStep 2 — Inverse demand: P = 60 − 2.5Q, so the price intercept (Q=0) is $60.\nStep 3 — CS triangle:\n  CS = ½ × 22 × ($60 − $5) = $605.\n\nThe club charges a $605/month membership fee + $5/court-hour. This extracts all consumer surplus while still allowing every welfare-improving trade (since P = MC).",
},
{
    "id": "m6-q2", "module": "M6", "theme": "3rd-Degree PD — Market A", "format": "open",
    "stem": "A firm sells a product in two markets it can keep separate. Market A: Q = 120 − 4P. Market B: Q = 80 − 2P. Marginal cost is constant at $6/unit.",
    "ask": "What is the profit-maximizing price in MARKET A (in $)?",
    "answer": 18, "tolerance_abs": 0.5, "unit": "$",
    "hints": [
        "Optimal 3rd-degree PD: in each market, set MR = MC separately.",
        "Inverse demand A: P = 30 − 0.25Q. MR_A = 30 − 0.5Q. Set MR = MC: 30 − 0.5Q = 6 → Q = 48. Then P = 30 − 0.25(48) = $18.",
        "Final answer: P_A = $18.",
    ],
    "solution": "Invert demand in A: from Q = 120 − 4P, P = 30 − 0.25Q.\nMR_A = 30 − 0.5Q.\n\nProfit-max: MR_A = MC\n  30 − 0.5Q = 6 → Q_A = 48\n  P_A = 30 − 0.25(48) = $18\n\n(Elasticity check at this point: e = (−4)·(18/48) = −1.5. |e| > 1, so the firm is operating in the elastic part of demand — as required.)",
},
{
    "id": "m6-q3", "module": "M6", "theme": "3rd-Degree PD — Market B", "format": "open",
    "stem": "Continuing the previous setup: Market B: Q = 80 − 2P. MC = $6/unit.",
    "ask": "What is the profit-maximizing price in MARKET B (in $)?",
    "answer": 23, "tolerance_abs": 0.5, "unit": "$",
    "hints": [
        "Same procedure: invert demand, derive MR, set MR = MC.",
        "Inverse demand B: P = 40 − 0.5Q. MR_B = 40 − Q. Set = MC: 40 − Q = 6 → Q_B = 34.",
        "P_B = 40 − 0.5(34) = $23.",
    ],
    "solution": "Inverse demand B: from Q = 80 − 2P, P = 40 − 0.5Q.\nMR_B = 40 − Q.\n\nMR_B = MC\n  40 − Q = 6 → Q_B = 34\n  P_B = 40 − 0.5(34) = $23.\n\nB has less elastic demand than A at the optimum (|e_B| = (−2)(23/34) ≈ 1.35 < 1.5), so the firm charges a HIGHER price in B ($23 vs $18). General rule: less-elastic market → higher price under 3rd-degree PD.",
},
{
    "id": "m6-q4", "module": "M6", "theme": "Conditions for 3rd-Degree PD", "format": "mcq",
    "stem": "A firm is considering third-degree price discrimination (charging different prices to different customer groups).",
    "ask": "Which of the following is NOT a required condition for it to work?",
    "choices": [
        "The firm has market power (downward-sloping demand)",
        "The firm can identify and separate customer groups",
        "Different groups have different price elasticities of demand",
        "All customers have identical willingness to pay",
        "The firm can prevent resale/arbitrage between groups",
    ],
    "correct_index": 3,
    "hints": [
        "Think about which condition would MAKE 3rd-degree PD worth doing vs which is required.",
        "If all customers had identical WTP, the firm would just set one optimal price — no need to discriminate.",
        "PD requires DIFFERENT elasticities across groups, market power, identifiable groups, and no-arbitrage — but not identical WTP. Identical WTP is the OPPOSITE of what PD requires.",
    ],
    "solution": "Required conditions for 3rd-degree PD:\n  ✓ Market power (else can't change P)\n  ✓ Identifiable groups (else can't separate)\n  ✓ Different price elasticities across groups (else no profit gain)\n  ✓ Prevent arbitrage (else low-price buyers resell to high-price buyers)\n\nNOT required (in fact, OPPOSITE):\n  ✗ Identical WTP — if all customers had the same WTP, there'd be no point segmenting.",
},
{
    "id": "m6-q5", "module": "M6", "theme": "Flat-Fee (Volume) Pricing", "format": "open",
    "stem": "A streaming music service faces per-subscriber demand Q = 40 − 2P, where Q is hours of listening per month and P is the per-hour price. The marginal cost of streaming is essentially zero. The service uses VOLUME PRICING — a flat monthly fee for unlimited access.",
    "ask": "What is the profit-maximizing flat monthly fee per subscriber (in $)?",
    "answer": 400, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "Volume pricing = two-part tariff with per-unit P = $0. The flat fee captures all consumer surplus at P = 0.",
        "At P = 0: Q = 40 hours. Inverse demand: from Q = 40 − 2P, P = 20 − 0.5Q, so at Q = 0, P = $20.",
        "CS = ½ × 40 × ($20 − $0) = $400. Charge this as the flat fee.",
    ],
    "solution": "With MC = 0, the firm maximizes revenue per subscriber, which equals the consumer surplus at the chosen per-unit price. The optimal per-unit price is $0 (let them consume their full demand), and the fee captures all surplus.\n\nAt P = $0: Q = 40 hours. Inverse demand price intercept = $20.\nCS = ½ × 40 × $20 = $400.\n\nFlat monthly fee = $400 per subscriber.\n\n(More than any per-unit pricing: at the standard monopoly point P=$5, Q=30, revenue per subscriber = $150. The flat fee extracts far more.)",
},
]

# =================== MODULE 7: Oligopoly & Game Theory ===================
QUESTIONS += [
{
    "id": "m7i-q1", "module": "M7-I", "theme": "Cournot Equilibrium Quantity", "format": "open",
    "stem": "Two firms compete in Cournot fashion (choosing quantities simultaneously). Inverse market demand is P = 120 − Q (where Q = q₁ + q₂). Both firms have constant MC = $30 and no fixed costs.",
    "ask": "What is each firm's equilibrium output?",
    "answer": 30, "tolerance_abs": 0.1, "unit": "",
    "hints": [
        "Each firm's reaction function: take the rival's q as given, write residual demand, set MR = MC.",
        "Firm 1's residual demand: P = (120 − q₂) − q₁. MR_1 = (120 − q₂) − 2q₁. Set = 30: q₁ = (90 − q₂)/2 = 45 − q₂/2.",
        "By symmetry, q₁ = q₂ = q*. Substitute: q* = 45 − q*/2 → 1.5 q* = 45 → q* = 30.",
    ],
    "solution": "Each firm's reaction function:\n  q_i = (a − MC − q_j) / 2  where a = 120\n      = (90 − q_j) / 2\n      = 45 − q_j/2\n\nSymmetric Nash equilibrium: q₁ = q₂ = q.\n  q = 45 − q/2\n  1.5 q = 45\n  q* = 30 each.\n\nTotal Q = 60. Market P = 120 − 60 = $60. Each firm's profit = (60 − 30) × 30 = $900.\n\n(For comparison: monopoly would set Q=45, P=$75, profit $2,025. Cournot industry profit is $1,800 — less than monopoly but more than PC's zero.)",
},
{
    "id": "m7i-q2", "module": "M7-I", "theme": "Cournot Market Price", "format": "open",
    "stem": "Same Cournot setup as the previous question (P = 120 − Q, MC = $30, two symmetric firms).",
    "ask": "What is the equilibrium market price (in $)?",
    "answer": 60, "tolerance_abs": 0.1, "unit": "$",
    "hints": [
        "Plug total equilibrium quantity into the demand curve.",
        "Each firm produces 30, so total Q = 60.",
        "P = 120 − 60 = $60.",
    ],
    "solution": "Q_total = q₁ + q₂ = 2 × 30 = 60.\n\nP = 120 − Q = 120 − 60 = $60.\n\nCompare with monopoly (P = $75) and perfect competition (P = MC = $30). Duopoly gives a price between these.",
},
{
    "id": "m7i-mcq-1", "module": "M7-I", "theme": "Bertrand Outcome", "format": "mcq",
    "stem": "Two firms produce identical products and compete in Bertrand fashion (choosing prices simultaneously). Both have constant MC = $8. There is no collusion.",
    "ask": "What is the equilibrium market price?",
    "choices": [
        "$8 (equal to marginal cost)",
        "The monopoly price",
        "Halfway between MC and the monopoly price",
        "Depends on the demand elasticity",
        "There is no pure-strategy equilibrium",
    ],
    "correct_index": 0,
    "hints": [
        "Identical products + price competition + same MC: classic Bertrand paradox setup.",
        "Each firm wants to undercut the other's price. As long as P > MC, undercutting is profitable. Where does undercutting stop?",
        "At P = MC = $8. Below that, neither firm wants to sell (would lose money). So the unique Nash equilibrium is P = $8.",
    ],
    "solution": "Bertrand competition with identical products and equal MC drives price down to MC.\n\nReasoning: as long as P > MC, each firm can profitably undercut the other and capture the whole market. This undercutting continues until P = MC = $8. Below that, neither firm would sell, so $8 is the floor.\n\nThis is the Bertrand paradox: with just two firms and identical products, we get the perfectly competitive outcome.",
},
{
    "id": "m7ii-mcq-1", "module": "M7-II", "theme": "Dominant Strategy / NE", "format": "mcq",
    "stem": "Two firms (A and B) simultaneously choose whether to CUT or HOLD their price. Payoffs (A's, B's):\n  Both hold: (30, 30)\n  A cuts, B holds: (38, 12)\n  A holds, B cuts: (12, 38)\n  Both cut: (20, 20)",
    "ask": "What is the Nash equilibrium?",
    "choices": [
        "Both cut",
        "Both hold",
        "A cuts, B holds",
        "B cuts, A holds",
        "There are two pure-strategy NE",
    ],
    "correct_index": 0,
    "hints": [
        "Find each player's best response to each of the other's choices. If a strategy is always the best response, it's dominant.",
        "A's payoffs: if B holds, A gets 38 (cut) vs 30 (hold) → cut. If B cuts, A gets 20 (cut) vs 12 (hold) → cut. So cutting dominates for A.",
        "Same logic for B. Both have dominant strategy 'cut'. NE = (Cut, Cut) with payoffs (20, 20). Classic Prisoner's Dilemma: both would prefer (30, 30) but neither can sustain it.",
    ],
    "solution": "Player A's analysis:\n  If B holds: A gets 38 (cut) vs 30 (hold) → choose cut.\n  If B cuts: A gets 20 (cut) vs 12 (hold) → choose cut.\n  → 'Cut' is A's DOMINANT strategy.\n\nBy symmetry, B's dominant strategy is also 'cut'.\n\nNash equilibrium: (Cut, Cut), payoffs (20, 20).\n\nClassic prisoner's dilemma: both players would prefer (Hold, Hold) = (30, 30), but each individually wants to deviate.",
},
{
    "id": "m7i-q3", "module": "M7-I", "theme": "Cartel vs Cournot", "format": "open",
    "stem": "Same Cournot setup (P = 120 − Q, MC = $30, two firms). If the two firms could form a cartel and split production equally, what would EACH firm produce?",
    "ask": "What is each firm's cartel output?",
    "answer": 22.5, "tolerance_abs": 0.5, "unit": "",
    "hints": [
        "A cartel acts as a single monopolist. Find total monopoly Q, then split.",
        "Monopoly: MR = 120 − 2Q = MC = 30 → Q_total = 45.",
        "Split equally: each firm produces 45 / 2 = 22.5.",
    ],
    "solution": "Cartel = joint monopoly. With combined output Q:\n  MR = 120 − 2Q. Set = MC = 30: Q* = 45.\n  P* = $75. Joint profit = (75 − 30) × 45 = $2,025.\n\nSplit equally: each firm produces 22.5 and earns $1,012.50.\n\nCompare to Cournot: each firm produced 30 and earned $900. The cartel is better for both firms BUT unstable: at the cartel quantity, each firm has incentive to cheat (best response to q_j = 22.5 is q_i = 45 − 11.25 = 33.75, not 22.5). This is why cartels are fragile.",
},
]

# =================== MODULE 8: Auctions ===================
QUESTIONS += [
{
    "id": "m8-q1", "module": "M8", "theme": "Second-Price Sealed Bid", "format": "open",
    "stem": "You are bidding in a second-price sealed-bid auction (the highest bidder wins but pays the SECOND-highest bid). Your private value for the item is $1,500. You expect the next-highest bidder values it at $1,100.",
    "ask": "What is your optimal bid (in $)?",
    "answer": 1500, "tolerance_abs": 0, "unit": "$",
    "hints": [
        "Recall the dominant strategy in second-price auctions.",
        "In a 2nd-price auction, bidding your TRUE VALUE is a dominant strategy — bidding higher risks paying more than the item is worth to you; bidding lower risks losing when you could have won at a profitable price.",
        "Bid your true value: $1,500. If you win, you pay the 2nd-highest bid ($1,100) → surplus = $1,500 − $1,100 = $400.",
    ],
    "solution": "Dominant strategy in 2nd-price sealed-bid auctions: bid your true value.\n\nWhy?\n  • If you bid above true value: you might win the auction but pay more than the item is worth → loss.\n  • If you bid below true value: you might lose to someone who values it less but bid higher than you → forgone profit.\n  • Bidding exactly your value: you win when (and only when) you're the highest valuer, and you pay the 2nd price — so winning is always weakly profitable.\n\nOptimal bid: $1,500. Expected payment if you win: $1,100. Expected surplus: $400.",
},
{
    "id": "m8-q2", "module": "M8", "theme": "First-Price Bidding (Symmetric)", "format": "open",
    "stem": "You're bidding in a first-price sealed-bid auction. Your private value is $80. You have ONE opponent whose value is independently drawn from a uniform distribution on [$0, $80]. Both bidders use the symmetric Bayes-Nash equilibrium strategy.",
    "ask": "What is your optimal bid (in $)?",
    "answer": 40, "tolerance_abs": 1, "unit": "$",
    "hints": [
        "In a first-price auction with n symmetric bidders, each with value uniformly drawn from [0, V], the equilibrium bid is ((n−1)/n) × your value.",
        "Here n = 2, so the optimal bid is ((2−1)/2) × your value = half your value.",
        "Bid = ½ × $80 = $40.",
    ],
    "solution": "In a first-price sealed-bid auction with n symmetric bidders (each value drawn IID from uniform [0, V_max]), the equilibrium bid is:\n  b(v) = ((n − 1) / n) × v\n\nFor n = 2: b(v) = v/2.\n\nYour bid: $80 / 2 = $40.\n\nIntuition: you SHADE your bid below your value because in first-price you pay what you bid. Bidding too low → low win probability. Bidding too high → win but small surplus. The optimum balances these.",
},
{
    "id": "m8-q3", "module": "M8", "theme": "Winner's Curse", "format": "mcq",
    "stem": "An energy company is bidding for the rights to develop an offshore wind tract. The true value depends on the wind resource and grid conditions — uncertain to all bidders, who each form their own estimate. This is a COMMON-VALUE auction.",
    "ask": "What is the recommended strategy to avoid the winner's curse?",
    "choices": [
        "Refuse to participate in common-value auctions — they're never profitable",
        "Bid randomly to confuse other bidders",
        "Bid your private estimate of the value — that's a dominant strategy",
        "Bid slightly above your estimate to ensure winning",
        "Shade your bid BELOW your estimate, and shade more when there are MORE bidders",
    ],
    "correct_index": 4,
    "hints": [
        "The 'winner's curse' refers to what happens to whoever wins a common-value auction.",
        "Whoever wins likely had the HIGHEST estimate among all bidders. If estimates are unbiased, the highest estimate is likely an OVERESTIMATE of the true value.",
        "To avoid systematically overpaying, shade your bid BELOW your estimate. The more bidders there are, the more extreme the winning estimate likely is — shade more aggressively.",
    ],
    "solution": "Winner's curse: in a common-value auction, the bidder with the highest estimate is the one most likely to have OVERESTIMATED the true value. Naively bidding your estimate leads to systematic overpayment.\n\nOptimal response: shade your bid BELOW your private estimate. With more bidders, the gap between the highest estimate and the true value grows on average, so shade more aggressively when n is large.\n\n(In private-value auctions like 1st-price, you also shade — but for a different reason: to balance win probability against surplus. The winner's-curse shading is on top of that strategic shading.)",
},
]

# Final consistency: every question has hints (3), solution, etc.
for q in QUESTIONS:
    assert "id" in q and "module" in q and "format" in q
    assert q["format"] in ("open", "mcq")
    assert "stem" in q and q["stem"], f"{q.get('id')} missing stem"
    assert "ask" in q and q["ask"], f"{q.get('id')} missing ask"
    assert "hints" in q and len(q["hints"]) == 3
    assert "solution" in q and q["solution"]
    if q["format"] == "open":
        assert "answer" in q
    else:
        assert "choices" in q and "correct_index" in q
