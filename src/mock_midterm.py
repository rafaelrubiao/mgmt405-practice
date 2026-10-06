"""Mock midterm for MGMT 405 (Modules 1-3), built into docs/mock-midterm.html.

Same format as the real midterm: Part 1 has 10 multiple-choice questions worth
3 points each; Part 2 has two problems worth 70 points. Every scenario and every
number here is new (nothing is taken from a past exam or from the practice bank).

Schema (validated by build_site.py):
  MOCK["mcqs"]      10 dicts: id, module, topic, stem, ask, choices (5), correct_index, solution
  MOCK["problems"]  dicts: id, title, points, intro, parts
  part              id, label, points, text, items, self_rubric, solution, figure (optional)
  item kinds        "select"  (options, correct index, points, rubric)
                    "number"  (answer, tolerance, points, rubric, unit optional)
                    "formula" (template with {key} slots, fields = number items with a key)
                    "text"    (free-text box, not graded)
  self_rubric       lines the student ticks after submitting (graph drawn, reasoning given)
Within each part, item points + self_rubric points must add up to the part's points.
Stems, asks and texts are plain text; **bold** is the only markup rendered.
"""

MOCK = {
    "slug": "mock-midterm",
    "state_key": "mgmt405_mock_midterm_v1",
    "title": "Mock Midterm Exam",
    "subtitle": "Managerial Economics (100 points)",
    "time_limit_minutes": 120,
    "mcq_points": 3,
    "rounding_note": "Please round all numbers to one decimal place (e.g., 43.6791 → 43.7). Enter a loss or a decrease as a negative number, and keep the sign of elasticities. Coefficients inside formulas can be entered exactly (e.g., 0.05).",
    "start_notes": [
        "Same format as the real midterm: Part 1 has 10 multiple-choice questions worth 3 points each (30 points); Part 2 has 2 problems worth 70 points. It covers Modules 1, 2 and 3.",
        "You have 2 hours. The clock starts when you click Take the Quiz and keeps running even if you close this page; the quiz is submitted automatically when the time is up.",
        "A calculator is allowed (a simple one is built into this page, bottom right). Keep paper and a pencil at hand: Problem 1 asks you to sketch supply and demand graphs on paper and to record on the page what shifts and what happens to price and quantity.",
        "Your answers are saved in this browser as you type, so you can reload the page without losing them. You can submit only once; after submitting you see your score, the correct answers, step-by-step solutions and the point rubric for every part. Nothing is sent anywhere.",
    ],
    "results_note": "Points for graphs and written explanations cannot be checked automatically. Compare your work with the solution and tick the rubric lines you got right; they are added to your total.",

    # ------------------------------------------------------------------ Part 1
    "mcqs": [
        {
            "id": "mock-mc1", "module": "Module 1", "topic": "Economic profit and implicit costs",
            "stem": "Priya left a job that paid her $85,000 a year to open a tutoring center. She runs it in a small building she owns, which she had been renting out to a shop for $24,000 a year. In its first year the center brought in $230,000 in revenue and paid $120,000 for instructors, utilities and materials.",
            "ask": "What was the tutoring center's economic profit in its first year?",
            "choices": ["−$23,000", "$1,000", "$25,000", "$86,000", "$110,000"],
            "correct_index": 1,
            "solution": "Accounting profit = revenue − explicit costs = 230,000 − 120,000 = $110,000.\n\nEconomic profit also subtracts the implicit costs, the value of what Priya gave up:\n  the salary from her old job: $85,000\n  the rent the building no longer earns: $24,000\n\nEconomic profit = 230,000 − 120,000 − 85,000 − 24,000 = $1,000.\n\nThe center only just beats her next-best alternatives. Leaving out the forgone rent gives $25,000; leaving out the forgone salary gives $86,000; leaving out both gives the accounting profit of $110,000.",
        },
        {
            "id": "mock-mc2", "module": "Module 1", "topic": "Marginal analysis (how many units)",
            "stem": "A catering company is deciding how many extra ovens to rent for the busy wedding season. Each oven rents for $400 per week. The company estimates the additional weekly profit, before paying the rent, that each extra oven would bring: the first oven $900, the second $700, the third $500, the fourth $450 and the fifth $200.",
            "ask": "How many ovens should the company rent?",
            "choices": ["2 ovens", "3 ovens", "4 ovens", "5 ovens", "As many as it can get, since every oven adds profit before rent"],
            "correct_index": 2,
            "solution": "Rent an oven if its marginal benefit (the extra profit before rent) is at least its marginal cost (the $400 rent).\n\nOven 1: $900 > $400, rent it. Oven 2: $700 > $400, rent it. Oven 3: $500 > $400, rent it. Oven 4: $450 > $400, rent it. Oven 5: $200 < $400, do not rent it.\n\nSo the company should rent 4 ovens. Net gain = (900 − 400) + (700 − 400) + (500 − 400) + (450 − 400) = $850 per week; a fifth oven would lose $200 per week.\n\nLooking at totals or averages misleads here: five ovens still give a positive total, but the fifth oven by itself does not pay for its rent.",
        },
        {
            "id": "mock-mc3", "module": "Module 1", "topic": "Reading a market change (shift or movement)",
            "stem": "Over the past year, both the average monthly rent and the number of apartments rented in a mid-sized city increased.",
            "ask": "Which single change in the rental market is consistent with both facts?",
            "choices": [
                "The demand for apartments increased, for example because more people moved to the city",
                "The supply of apartments increased, for example because new buildings were completed",
                "The demand for apartments decreased, for example because people moved away",
                "The supply of apartments decreased, for example because buildings were converted to hotels",
                "Both the supply of and the demand for apartments decreased",
            ],
            "correct_index": 0,
            "solution": "Work backwards from what happened to price and quantity.\n\nA demand increase raises both the price and the quantity: consistent with higher rents and more apartments rented.\nA supply increase raises the quantity but lowers the price.\nA demand decrease lowers both.\nA supply decrease raises the price but lowers the quantity.\nIf both curves shift left, the quantity falls for sure.\n\nOnly an increase in demand fits a higher rent together with more apartments rented.",
        },
        {
            "id": "mock-mc4", "module": "Module 2", "topic": "Using elasticity to hit a target",
            "stem": "A city estimates that the price elasticity of demand for downtown parking is −0.3. To reduce congestion, it wants to cut the number of cars parking downtown by 6%.",
            "ask": "By roughly how much should the city raise its parking rates to reach this target?",
            "choices": ["1.8%", "6%", "12%", "20%", "60%"],
            "correct_index": 3,
            "solution": "Elasticity = %ΔQ / %ΔP. Rearranging, %ΔP = %ΔQ / elasticity = (−6%) / (−0.3) = +20%.\n\nBecause demand is inelastic (0.3 in absolute value), the price has to rise by much more than the desired fall in quantity.\n\nCheck: a 20% price increase × (−0.3) = −6%.",
        },
        {
            "id": "mock-mc5", "module": "Module 2", "topic": "Marginal revenue of one more unit",
            "stem": "A small knife workshop sells 100 chef's knives per month at $50 each. Its owner believes that to sell one more knife per month she would have to lower the price to $49.60, and that the lower price would apply to all the knives she sells.",
            "ask": "What is the marginal revenue of the 101st knife?",
            "choices": ["−$40.00", "$9.60", "$40.00", "$49.60", "$50.00"],
            "correct_index": 1,
            "solution": "Marginal revenue is the change in total revenue from selling one more unit.\n\nRevenue now: 100 × $50 = $5,000.\nRevenue with 101 knives: 101 × $49.60 = $5,009.60.\nMarginal revenue = 5,009.60 − 5,000 = $9.60.\n\nIt is far below the $49.60 price because the $0.40 price cut is lost on the 100 knives that were already selling (100 × $0.40 = $40): $49.60 − $40 = $9.60. This is why marginal revenue lies below the demand curve.",
        },
        {
            "id": "mock-mc6", "module": "Module 2", "topic": "Elasticity and total revenue",
            "stem": "A city museum raised its admission price from $20 to $23. Weekly attendance fell from 4,000 to 3,760 visitors. Nothing else about the museum or its competitors changed.",
            "ask": "Based on these numbers, how would you describe demand at the original price, and what happened to the museum's weekly admission revenue?",
            "choices": [
                "Demand is elastic; revenue fell",
                "Demand is elastic; revenue rose",
                "Demand is unit elastic; revenue did not change",
                "Demand is inelastic; revenue fell",
                "Demand is inelastic; revenue rose",
            ],
            "correct_index": 4,
            "solution": "Percentage changes relative to the initial point:\n%ΔP = (23 − 20) / 20 = +15%.\n%ΔQ = (3,760 − 4,000) / 4,000 = −6%.\n\nElasticity = −6% / 15% = −0.4. Its absolute value is below 1, so demand is inelastic.\n\nRevenue before: $20 × 4,000 = $80,000 per week. Revenue after: $23 × 3,760 = $86,480 per week. Revenue rose by $6,480 (8.1%).\n\nWith inelastic demand the quantity lost is proportionally smaller than the price gained, so a price increase raises revenue.",
        },
        {
            "id": "mock-mc7", "module": "Module 3", "topic": "Marginal cost",
            "stem": "A small manufacturer is choosing between two loan offers from its bank: borrow $200,000 at an annual interest rate of 4.5%, or borrow $240,000 at an annual interest rate of 5.0%. The firm needs at least $200,000 and is deciding whether the extra $40,000 is worth taking.",
            "ask": "What is the marginal annual interest rate on the additional $40,000?",
            "choices": ["0.5%", "4.5%", "4.75%", "5.0%", "7.5%"],
            "correct_index": 4,
            "solution": "Marginal cost is the extra cost of the extra unit, here the extra $40,000 of borrowing.\n\nInterest on $200,000 at 4.5% = $9,000 per year.\nInterest on $240,000 at 5.0% = $12,000 per year.\nExtra interest = $3,000 per year for an extra $40,000 of loan.\n\nMarginal interest rate = 3,000 / 40,000 = 7.5% per year.\n\nThe average rate on the larger loan is 5%, but the extra $40,000 costs 7.5% because the higher rate applies to the whole loan, not only to the additional amount.",
        },
        {
            "id": "mock-mc8", "module": "Module 3", "topic": "Marginal and average product",
            "stem": "A customer-support call center recorded how many calls it can answer per day with different numbers of agents on duty (all other inputs fixed):\n\n  5 agents: 400 calls per day\n  6 agents: 470 calls per day\n  7 agents: 520 calls per day",
            "ask": "What is the marginal product of the seventh agent, and what happens to the average product per agent when the seventh agent is added?",
            "choices": [
                "20 calls; average product falls",
                "50 calls; average product rises",
                "50 calls; average product falls",
                "74.3 calls; average product rises",
                "520 calls; average product is unchanged",
            ],
            "correct_index": 2,
            "solution": "Marginal product = the extra calls from one extra agent.\nMP of the 7th agent = 520 − 470 = 50 calls per day. (The 6th agent added 70, so returns are diminishing.)\n\nAverage product = calls per agent.\nWith 6 agents: 470 / 6 = 78.3 calls per agent. With 7 agents: 520 / 7 = 74.3 calls per agent.\n\nThe 7th agent's marginal product (50) is below the average of the first six (78.3), so the average is pulled down.",
        },
        {
            "id": "mock-mc9", "module": "Module 3", "topic": "Make or buy (relevant costs)",
            "stem": "A lamp manufacturer needs 2,000 metal lamp bases this year. Making them in-house costs $14 per base in materials and labor. Last year the firm also paid $12,000 for the tooling needed to make the bases; the tooling cannot be resold or refunded. A supplier now offers to deliver the same bases for $18 each.",
            "ask": "Should the firm make or buy the bases, and by how much does the better option improve this year's profit compared with the other?",
            "choices": [
                "Buy: it saves $4,000",
                "Buy: it saves $8,000",
                "Either: the two options cost the same",
                "Make: it saves $8,000",
                "Make: it saves $20,000",
            ],
            "correct_index": 3,
            "solution": "Only costs that change with the decision matter.\n\nThe $12,000 tooling was paid last year and cannot be recovered: it is a sunk cost, the same whether the firm makes or buys, so it is ignored.\n\nMaking: 2,000 × $14 = $28,000. Buying: 2,000 × $18 = $36,000.\n\nMaking is cheaper by $8,000, so the firm should make the bases. (Adding the sunk $12,000 to the make option would give $40,000 and wrongly point to buying.)",
        },
        {
            "id": "mock-mc10", "module": "Module 3", "topic": "Marginal versus average cost",
            "stem": "A sign maker's total cost is $5,000 per week when it produces 100 signs and $5,030 per week when it produces 101 signs. Its fixed costs are $2,000 per week.",
            "ask": "What is the marginal cost of the 101st sign, and how does it compare with the average total cost of producing 100 signs?",
            "choices": [
                "$30; below the average total cost",
                "$30; above the average total cost",
                "$50; equal to the average total cost",
                "$50; above the average total cost",
                "$5,030; above the average total cost",
            ],
            "correct_index": 0,
            "solution": "Marginal cost = the change in total cost from one more unit = 5,030 − 5,000 = $30.\n\nAverage total cost at 100 signs = 5,000 / 100 = $50 (made up of $20 of average fixed cost and $30 of average variable cost).\n\nThe marginal cost ($30) is below the average total cost ($50), so producing the 101st sign pulls the average down (to 5,030 / 101 = $49.80). Fixed costs play no role in the marginal cost.",
        },
    ],

    # ------------------------------------------------------------------ Part 2
    "problems": [
        {
            "id": "mock-p1",
            "title": "Cocoa, chocolate and the snack aisle",
            "points": 20,
            "intro": "Cocoa beans are the main ingredient of chocolate, and most of the world's cocoa is grown in West Africa. In 2024, crop disease and poor weather sharply reduced the West African cocoa harvest. In this problem, follow the effects of this harvest shock through three markets. In each market, treat the change described as the only change (all else equal), and sketch your graphs on paper.",
            "parts": [
                {
                    "id": "mock-p1a", "label": "(a)", "points": 6,
                    "text": "The world market for cocoa beans. Draw the market before and after the harvest shock. Which curve shifts, and in which direction? What happens to the equilibrium price and quantity of cocoa beans? Explain in words.",
                    "items": [
                        {"id": "mock-p1a-shift", "kind": "select", "points": 2,
                         "label": "Which curve shifts, and in which direction?",
                         "options": ["Demand shifts to the right", "Demand shifts to the left", "Supply shifts to the right", "Supply shifts to the left", "Both curves shift", "No curve shifts; there is only a movement along the curves"],
                         "correct": 3, "rubric": "Supply shifts to the left"},
                        {"id": "mock-p1a-price", "kind": "select", "points": 1,
                         "label": "Equilibrium price of cocoa beans",
                         "options": ["Rises", "Falls", "Ambiguous (depends on the size of the shifts)"],
                         "correct": 0, "rubric": "Price rises"},
                        {"id": "mock-p1a-qty", "kind": "select", "points": 1,
                         "label": "Equilibrium quantity of cocoa beans",
                         "options": ["Rises", "Falls", "Ambiguous (depends on the size of the shifts)"],
                         "correct": 1, "rubric": "Quantity falls"},
                        {"id": "mock-p1a-expl", "kind": "text", "label": "Explain in words", "rows": 4},
                    ],
                    "self_rubric": [
                        {"id": "mock-p1a-graph", "points": 1, "text": "Graph: downward-sloping demand, upward-sloping supply, the initial equilibrium and the new equilibrium marked"},
                        {"id": "mock-p1a-reason", "points": 1, "text": "Explanation: a smaller harvest means less cocoa is offered at every price, so the market moves up along the demand curve to a higher price and a lower quantity"},
                    ],
                    "solution": "The harvest shock reduces the quantity of cocoa offered at every price: the supply curve shifts to the left (from S to S').\n\nAt the old price there is now excess demand, so the price rises and the market moves up along the demand curve to the new equilibrium E': the equilibrium price of cocoa rises and the equilibrium quantity falls.\n\nRubric: 2 points for the shift, 2 for price and quantity, 1 for the graph, 1 for the explanation.",
                    "figure": {"kind": "sd", "title": "(a) Cocoa beans: supply shifts left", "d": [90], "s": [10, 30]},
                },
                {
                    "id": "mock-p1b", "label": "(b)", "points": 8,
                    "text": "The market for chocolate bars. Chocolate makers buy cocoa at the market price. Explain how the change in part (a) affects the market for chocolate bars: which curve shifts, why, and what happens to the equilibrium price and quantity of chocolate bars? Draw the market before and after. Also say whether this is a shift of a curve or a movement along a curve.",
                    "items": [
                        {"id": "mock-p1b-shift", "kind": "select", "points": 3,
                         "label": "Which curve shifts, and in which direction?",
                         "options": ["Demand shifts to the right", "Demand shifts to the left", "Supply shifts to the right", "Supply shifts to the left", "Both curves shift", "No curve shifts; there is only a movement along the curves"],
                         "correct": 3, "rubric": "Supply of chocolate bars shifts to the left (the input got more expensive)"},
                        {"id": "mock-p1b-price", "kind": "select", "points": 1,
                         "label": "Equilibrium price of chocolate bars",
                         "options": ["Rises", "Falls", "Ambiguous (depends on the size of the shifts)"],
                         "correct": 0, "rubric": "Price rises"},
                        {"id": "mock-p1b-qty", "kind": "select", "points": 1,
                         "label": "Equilibrium quantity of chocolate bars",
                         "options": ["Rises", "Falls", "Ambiguous (depends on the size of the shifts)"],
                         "correct": 1, "rubric": "Quantity falls"},
                        {"id": "mock-p1b-kind", "kind": "select", "points": 1,
                         "label": "What happens to the supply side is best described as",
                         "options": ["A shift of the supply curve", "A movement along the supply curve", "A shift of the demand curve", "A movement along the demand curve"],
                         "correct": 0, "rubric": "A shift of the supply curve (an input price changed, not the price of chocolate)"},
                        {"id": "mock-p1b-expl", "kind": "text", "label": "Explain in words", "rows": 4},
                    ],
                    "self_rubric": [
                        {"id": "mock-p1b-graph", "points": 1, "text": "Graph: demand and supply for chocolate bars, the initial equilibrium and the new equilibrium marked"},
                        {"id": "mock-p1b-reason", "points": 1, "text": "Explanation: cocoa is an input, so the higher cocoa price raises the cost of making chocolate; at every chocolate price makers offer fewer bars"},
                    ],
                    "solution": "Cocoa is an input for chocolate. The higher cocoa price raises the cost of producing chocolate, so at every price of chocolate, makers are willing to supply fewer bars: the supply curve of chocolate bars shifts to the left.\n\nThis is a shift of the supply curve, not a movement along it: the curve moves because an input price changed, not because the price of chocolate changed. (The price of chocolate then changes as a result, and buyers move along the demand curve.)\n\nNew equilibrium: a higher price of chocolate bars and a lower quantity.\n\nRubric: 3 points for the shift and its direction, 2 for price and quantity, 1 for shift versus movement, 1 for the graph, 1 for the explanation.",
                    "figure": {"kind": "sd", "title": "(b) Chocolate bars: supply shifts left", "d": [90], "s": [10, 30]},
                },
                {
                    "id": "mock-p1c", "label": "(c)", "points": 6,
                    "text": "The market for fruit gummies, a popular alternative to chocolate bars. (i) What does the higher price of chocolate bars do to the market for fruit gummies: which curve shifts, and in which direction? (ii) Now suppose that at the same time the price of sugar, the main input for gummies, falls. Taking both changes together, what can you say for certain about the equilibrium price and quantity of fruit gummies, and what is ambiguous? Explain why. (No graph is required, but you may use one.)",
                    "items": [
                        {"id": "mock-p1c-shift", "kind": "select", "points": 2,
                         "label": "(i) Effect of the higher chocolate price on the gummies market",
                         "options": ["Demand shifts to the right", "Demand shifts to the left", "Supply shifts to the right", "Supply shifts to the left", "No curve shifts; there is only a movement along the curves"],
                         "correct": 0, "rubric": "Demand for gummies shifts to the right (chocolate and gummies are substitutes)"},
                        {"id": "mock-p1c-price", "kind": "select", "points": 1.5,
                         "label": "(ii) Equilibrium price of gummies, both changes together",
                         "options": ["Rises", "Falls", "Ambiguous (depends on the size of the shifts)"],
                         "correct": 2, "rubric": "Price: ambiguous"},
                        {"id": "mock-p1c-qty", "kind": "select", "points": 1.5,
                         "label": "(ii) Equilibrium quantity of gummies, both changes together",
                         "options": ["Rises", "Falls", "Ambiguous (depends on the size of the shifts)"],
                         "correct": 0, "rubric": "Quantity rises"},
                        {"id": "mock-p1c-expl", "kind": "text", "label": "Explain why", "rows": 4},
                    ],
                    "self_rubric": [
                        {"id": "mock-p1c-reason", "points": 1, "text": "Explanation: both changes raise the quantity; the demand shift pushes the price up and the supply shift pushes it down, so the price depends on which shift is larger"},
                    ],
                    "solution": "(i) Chocolate bars and fruit gummies are substitutes. When chocolate gets more expensive, some consumers switch to gummies: at every price of gummies, more are demanded, so the demand curve for gummies shifts to the right (on its own this raises both the price and the quantity of gummies).\n\n(ii) Cheaper sugar lowers the cost of making gummies: the supply curve shifts to the right (on its own this lowers the price and raises the quantity).\n\nTogether: both shifts raise the quantity, so the quantity of gummies rises for sure. The demand shift pushes the price up and the supply shift pushes it down, so the net effect on the price is ambiguous: it depends on which shift is larger (left panel: the supply shift dominates and the price falls; right panel: the demand shift dominates and the price rises).\n\nRubric: 2 points for the demand shift, 3 for price and quantity, 1 for the explanation.",
                    "figure": {"kind": "sd2",
                               "panels": [{"title": "Supply shift larger: price falls", "d": [80, 90], "s": [20, 0]},
                                          {"title": "Demand shift larger: price rises", "d": [80, 100], "s": [20, 10]}]},
                },
            ],
        },
        {
            "id": "mock-p2",
            "title": "StandWell: a price test, elasticity and marginal revenue",
            "points": 50,
            "intro": "StandWell sells an adjustable standing desk online. At its regular price of $200 it sells 2,000 desks per month. To learn about its demand, the company ran a one-month price test: at a price of $180 it sold 2,400 desks. Nothing else changed during the test (same marketing, no seasonal effects). Treat the regular price of $200 as the initial situation.",
            "parts": [
                {
                    "id": "mock-p2a", "label": "(a)", "points": 8,
                    "text": "Using the two observations, compute the price elasticity of demand at the regular price of $200. Is demand elastic, inelastic or unit elastic at this price?",
                    "items": [
                        {"id": "mock-p2a-e", "kind": "number", "points": 4, "label": "Price elasticity of demand at P = $200", "answer": -2, "tolerance": 0.06, "rubric": "Elasticity = (+20%) / (−10%) = −2"},
                        {"id": "mock-p2a-type", "kind": "select", "points": 2, "label": "At this price, demand is", "options": ["Elastic", "Inelastic", "Unit elastic"], "correct": 0, "rubric": "Demand is elastic (absolute value above 1)"},
                    ],
                    "self_rubric": [
                        {"id": "mock-p2a-formula", "points": 2, "text": "Uses elasticity = %ΔQ / %ΔP, with both percentage changes measured from the initial point (P = $200, Q = 2,000)"},
                    ],
                    "solution": "Percentage changes from the initial point:\n%ΔP = (180 − 200) / 200 = −10%.\n%ΔQ = (2,400 − 2,000) / 2,000 = +20%.\n\nElasticity = %ΔQ / %ΔP = 20% / (−10%) = −2.\n\n|E| = 2 > 1: demand is elastic at the regular price. A 1% price cut raises the quantity sold by about 2%.\n\nRubric: 4 points for the formula and reasoning, 4 points for the number and the classification.",
                },
                {
                    "id": "mock-p2b", "label": "(b)", "points": 8,
                    "text": "Assume that the demand for the desk is linear. Use the two observations to derive the demand function, with quantity Q (desks per month) as a function of the price P (in dollars).",
                    "items": [
                        {"id": "mock-p2b-dem", "kind": "formula", "points": 6, "label": "Demand function", "template": "Q = {a} − {b} × P",
                         "fields": [{"key": "a", "id": "mock-p2b-dem-a", "points": 3, "answer": 6000, "tolerance": 0.5},
                                    {"key": "b", "id": "mock-p2b-dem-b", "points": 3, "answer": 20, "tolerance": 0.005}],
                         "rubric": "Demand: Q = 6,000 − 20 × P"},
                    ],
                    "self_rubric": [
                        {"id": "mock-p2b-method", "points": 2, "text": "Method: slope from the two points, ΔQ/ΔP = 400 / (−20) = −20; intercept by plugging one of the points into Q = a − 20P"},
                    ],
                    "solution": "A linear demand function has the form Q = a − b × P.\n\nSlope: b = −ΔQ/ΔP = −(2,400 − 2,000) / (180 − 200) = −400 / (−20) = 20, so each extra dollar of price costs 20 desks per month: Q = a − 20P.\n\nIntercept: plug in the regular point: 2,000 = a − 20 × 200, so a = 6,000.\n\nDemand function: Q = 6,000 − 20 × P. Check with the test point: 6,000 − 20 × 180 = 2,400.\n\n(Consistency check with part a: at P = 200 the point elasticity is −20 × 200 / 2,000 = −2, the same number, because demand is linear.)\n\nRubric: 3 points for the slope, 3 for the intercept, 2 for the method.",
                },
                {
                    "id": "mock-p2c", "label": "(c)", "points": 10,
                    "text": "Compute StandWell's total revenue per month at the regular price of $200 and at the test price of $180, and the change in revenue. Which of the two prices brings in more revenue, and why?",
                    "items": [
                        {"id": "mock-p2c-tr0", "kind": "number", "points": 3, "label": "Total revenue at P = $200", "unit": "$ per month", "answer": 200 * 2000, "tolerance": 1, "rubric": "Revenue at $200: 200 × 2,000 = $400,000"},
                        {"id": "mock-p2c-tr1", "kind": "number", "points": 3, "label": "Total revenue at P = $180", "unit": "$ per month", "answer": 180 * 2400, "tolerance": 1, "rubric": "Revenue at $180: 180 × 2,400 = $432,000"},
                        {"id": "mock-p2c-dtr", "kind": "number", "points": 2, "label": "Change in revenue from cutting the price to $180", "unit": "$ per month", "answer": 180 * 2400 - 200 * 2000, "tolerance": 1, "rubric": "Change: 432,000 − 400,000 = +$32,000"},
                        {"id": "mock-p2c-which", "kind": "select", "points": 1, "label": "Which price brings in more revenue?", "options": ["$200", "$180", "They bring in the same revenue"], "correct": 1, "rubric": "The lower price, $180"},
                        {"id": "mock-p2c-expl", "kind": "text", "label": "Why?", "rows": 3},
                    ],
                    "self_rubric": [
                        {"id": "mock-p2c-reason", "points": 1, "text": "Links the result to elastic demand: the 20% gain in quantity outweighs the 10% price cut, so revenue rises"},
                    ],
                    "solution": "At the regular price: 200 × 2,000 = $400,000 per month.\nAt the test price: 180 × 2,400 = $432,000 per month.\nChange: 432,000 − 400,000 = +$32,000 per month (+8%).\n\nThe lower price brings in more revenue because demand is elastic at $200: the quantity sold rises by 20%, more than the 10% fall in price, so the extra units more than make up for the lower price on every unit.\n\nRubric: 3 points for each revenue figure, 2 for the change, 1 for the comparison, 1 for the reason.",
                },
                {
                    "id": "mock-p2d", "label": "(d)", "points": 12,
                    "text": "Using the demand function from (b), derive marginal revenue as a function of the quantity sold, and compute marginal revenue at the regular price (where Q = 2,000). Interpret the number you obtain.",
                    "items": [
                        {"id": "mock-p2d-inv", "kind": "formula", "points": 3, "label": "Inverse demand function", "template": "P = {a} − {b} × Q",
                         "fields": [{"key": "a", "id": "mock-p2d-inv-a", "points": 1.5, "answer": 300, "tolerance": 0.5},
                                    {"key": "b", "id": "mock-p2d-inv-b", "points": 1.5, "answer": 0.05, "tolerance": 0.0005}],
                         "rubric": "Inverse demand: P = 300 − 0.05 × Q"},
                        {"id": "mock-p2d-tr", "kind": "formula", "points": 3, "label": "Total revenue as a function of Q", "template": "TR = {a} × Q − {b} × Q²",
                         "fields": [{"key": "a", "id": "mock-p2d-tr-a", "points": 1.5, "answer": 300, "tolerance": 0.5},
                                    {"key": "b", "id": "mock-p2d-tr-b", "points": 1.5, "answer": 0.05, "tolerance": 0.0005}],
                         "rubric": "Total revenue: TR = 300 × Q − 0.05 × Q²"},
                        {"id": "mock-p2d-mr", "kind": "formula", "points": 3, "label": "Marginal revenue as a function of Q", "template": "MR = {a} − {b} × Q",
                         "fields": [{"key": "a", "id": "mock-p2d-mr-a", "points": 1.5, "answer": 300, "tolerance": 0.5},
                                    {"key": "b", "id": "mock-p2d-mr-b", "points": 1.5, "answer": 0.1, "tolerance": 0.0005}],
                         "rubric": "Marginal revenue: MR = 300 − 0.1 × Q"},
                        {"id": "mock-p2d-mr0", "kind": "number", "points": 2, "label": "Marginal revenue at Q = 2,000", "unit": "$", "answer": 300 - 0.1 * 2000, "tolerance": 0.5, "rubric": "At Q = 2,000: MR = 300 − 0.1 × 2,000 = $100"},
                        {"id": "mock-p2d-interp", "kind": "text", "label": "Interpret this number", "rows": 3},
                    ],
                    "self_rubric": [
                        {"id": "mock-p2d-interp-r", "points": 1, "text": "Interpretation: selling one more desk per month adds about $100 to monthly revenue, half the $200 price, because the small price cut needed to sell it applies to all 2,000 desks"},
                    ],
                    "solution": "Step 1, inverse demand (price as a function of quantity): from Q = 6,000 − 20P, 20P = 6,000 − Q, so P = 300 − 0.05 × Q.\n\nStep 2, total revenue: TR = P × Q = (300 − 0.05 × Q) × Q = 300 × Q − 0.05 × Q².\n\nStep 3, marginal revenue is the derivative of total revenue with respect to Q: MR = 300 − 0.1 × Q (same intercept as the inverse demand, twice the slope).\n\nStep 4, at the regular price Q = 2,000: MR = 300 − 0.1 × 2,000 = $100.\n\nInterpretation: at the regular price, selling one more desk per month raises monthly revenue by about $100, only half of the $200 price. To sell one more desk, StandWell must lower the price a little, and the lower price applies to all 2,000 desks it already sells. Marginal revenue is positive, consistent with elastic demand at this price.\n\nRubric: 3 points for the inverse demand, 3 for total revenue, 3 for marginal revenue, 3 for the number and its interpretation.",
                    "figure": {"kind": "dmr", "a": 300, "b": 0.05, "xlabel": "Desks per month",
                               "points": [{"q": 2000, "p": 200, "label": "regular price: P = $200, Q = 2,000"}, {"q": 3000, "p": 150, "label": "MR = 0: P = $150, Q = 3,000"}],
                               "mrpoint": {"q": 2000, "mr": 100, "label": "MR = $100"},
                               "mc": {"value": 60, "label": "MC = $60", "point_label": "MR = MC"}},
                },
                {
                    "id": "mock-p2e", "label": "(e)", "points": 6,
                    "text": "Which quantity and which price would maximize StandWell's total revenue?",
                    "items": [
                        {"id": "mock-p2e-q", "kind": "number", "points": 2, "label": "Revenue-maximizing quantity", "unit": "desks per month", "answer": 3000, "tolerance": 0.5, "rubric": "MR = 0 at Q = 300 / 0.1 = 3,000"},
                        {"id": "mock-p2e-p", "kind": "number", "points": 2, "label": "Revenue-maximizing price", "unit": "$", "answer": 150, "tolerance": 0.05, "rubric": "Price from inverse demand: 300 − 0.05 × 3,000 = $150"},
                    ],
                    "self_rubric": [
                        {"id": "mock-p2e-cond", "points": 2, "text": "States that total revenue is maximized where marginal revenue equals zero (MR = 0)"},
                    ],
                    "solution": "Total revenue is maximized where marginal revenue is zero: adding desks raises revenue as long as MR > 0 and lowers it once MR < 0.\n\nMR = 300 − 0.1 × Q = 0 gives Q = 3,000 desks per month.\n\nThe price that sells this quantity comes from the inverse demand: P = 300 − 0.05 × 3,000 = $150.\n\nCheck: at P = $150 the elasticity is −20 × 150 / 3,000 = −1 (unit elastic), as it must be at the revenue maximum. Revenue there is 150 × 3,000 = $450,000, above the $432,000 earned at $180.\n\nRubric: 2 points for saying that revenue is maximized where MR = 0, 2 for the quantity, 2 for the price.",
                },
                {
                    "id": "mock-p2f", "label": "(f)", "points": 6,
                    "text": "StandWell's marginal cost of producing and delivering a desk is $60 and does not change with the number of desks sold. Should the company lower its price all the way to the revenue-maximizing price from (e)? Compared with the regular price of $200, should the profit-maximizing price be higher or lower? Explain using marginal revenue and marginal cost.",
                    "items": [
                        {"id": "mock-p2f-all", "kind": "select", "points": 1, "label": "Lower the price all the way to the revenue-maximizing price?", "options": ["Yes", "No"], "correct": 1, "rubric": "No: at the revenue maximum MR = 0 is below the marginal cost"},
                        {"id": "mock-p2f-vs200", "kind": "select", "points": 2, "label": "Compared with the regular price of $200, the profit-maximizing price is", "options": ["Higher", "Lower", "The same"], "correct": 1, "rubric": "Lower: at Q = 2,000, MR = $100 is above MC = $60, so selling more adds profit"},
                        {"id": "mock-p2f-vsmax", "kind": "select", "points": 1, "label": "Compared with the revenue-maximizing price from (e), the profit-maximizing price is", "options": ["Higher", "Lower", "The same"], "correct": 0, "rubric": "Higher: the company should stop before MR falls to zero"},
                        {"id": "mock-p2f-expl", "kind": "text", "label": "Explain why", "rows": 3},
                    ],
                    "self_rubric": [
                        {"id": "mock-p2f-reason", "points": 2, "text": "Reasoning with MR and MC: profit rises as long as the next desk adds more revenue than cost (MR > MC); at Q = 2,000, MR = $100 > $60, so sell more (lower the price); at the revenue maximum MR = 0 < $60, so that is too far"},
                    ],
                    "solution": "Profit rises when selling one more desk adds more revenue than cost (MR > MC) and falls when it adds less (MR < MC).\n\nAt the regular price, Q = 2,000 and MR = $100, above the $60 marginal cost: the next desks add to profit, so StandWell should sell more, which means a price below $200.\n\nBut it should not go all the way to the revenue-maximizing price: there MR = 0, below the $60 marginal cost, so the last desks sold would cost more than they bring in. The best price is therefore below $200 but above $150.\n\n(For the curious: setting MR = MC, 300 − 0.1 × Q = 60 gives Q = 2,400 and P = $180, exactly the test price. You will study this rule in detail in Module 5.)\n\nRubric: 1 point for no, 2 for a lower price than $200, 1 for a higher price than the revenue maximum, 2 for the marginal revenue versus marginal cost reasoning.",
                },
            ],
        },
    ],
}
