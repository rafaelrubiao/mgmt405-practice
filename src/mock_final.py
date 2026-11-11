"""Mock final for MGMT 405 (all modules), built into docs/mock-final.html.

Same format as the real final: Part 1 has 20 multiple-choice questions worth
2 points each (graded automatically); Part 2 has three problems worth 60 points,
answered in free text and graded by the student with the rubric shown after
submission. The topic mix follows the Sample Final 2025. Every scenario and every
number here is new (nothing is taken from a past exam, the Sample Final or the
practice bank). The page is unlisted on the site.

Schema: the same as src/mock_midterm.py (see the top of that file).
"""

MOCK = {
    "slug": "mock-final",
    "state_key": "mgmt405_mock_final_v1",
    "name": "Mock Final",
    "header_sub": "All modules · 100 points · no time limit · same format as the real final",
    "covers": "All modules (1 to 8), with most weight on Modules 4 to 8",
    "n_mcqs": 20,
    "title": "Mock Final Exam",
    "subtitle": "Managerial Economics (100 points)",
    "time_limit_minutes": None,   # untimed practice; the real final has 3 hours
    "time_note": "None: come back to it as often as you like. **In the real final you will have 3 hours.**",
    "mcq_points": 2,
    "rounding_note": "Please round all numbers to two decimal places (e.g., 43.6791 → 43.68). Enter a loss or a decrease as a negative number, and keep the sign of elasticities.",
    "start_notes": [
        "Same format as the real final: Part 1 has 20 multiple-choice questions worth 2 points each (40 points); Part 2 has 3 problems worth 60 points. It covers all modules, with most weight on Modules 4 to 8.",
        "There is no time limit: you can stop, close the page and come back any time, as with the practice exercises. In the real final you will have **3 hours**, so if you want a realistic test, try to finish in one sitting of 3 hours.",
        "A calculator is allowed (a simple one is built into this page, bottom right). Part 2 has a writing box under each part: write your numbers and your reasoning there, as you would on paper in the real exam.",
        "Your answers are saved in this browser as you type, so you can reload the page without losing them. You can submit only once. After submitting you see your Part 1 score (graded automatically), the correct answers, step-by-step solutions, and the point rubric for Part 2, which you grade yourself. Nothing is sent anywhere.",
    ],
    "results_note": "Part 2 is not graded automatically. Compare what you wrote with the solution of each part and tick the rubric lines you got right; the points are added to your Part 2 score below.",

    # ------------------------------------------------------------------ Part 1
    "mcqs": [
        {
            "id": "mockf-mc1", "module": "Module 1", "topic": "Income and an inferior good",
            "stem": "In a large city, intercity bus rides are an inferior good: when people's incomes rise, they buy fewer bus tickets and travel by car or plane instead. Over the past two years, incomes in the city rose. Nothing else changed in the market for bus rides.",
            "ask": "What happened to the equilibrium price and the equilibrium quantity of bus rides?",
            "choices": [
                "Both the price and the quantity rose",
                "Both the price and the quantity fell",
                "The price rose and the quantity fell",
                "The price fell and the quantity rose",
                "Neither changed, because the supply of bus rides did not change",
            ],
            "correct_index": 1,
            "solution": "For an inferior good, higher income lowers the quantity demanded at every price: the demand curve shifts to the left.\n\nWith supply unchanged, the market moves down along the supply curve: the equilibrium price falls and the equilibrium quantity falls.\n\nA price rise with a quantity fall would come from a supply decrease; a price fall with a quantity rise would come from a supply increase.",
        },
        {
            "id": "mockf-mc2", "module": "Module 2", "topic": "Cross-price elasticity",
            "stem": "A market study finds that when the monthly price of a popular video streaming service rose by 10%, the number of movie theater tickets sold in the same region rose by 4%, with nothing else changing.",
            "ask": "What is the cross-price elasticity of movie tickets with respect to the streaming price, and how are the two goods related?",
            "choices": [
                "−0.4; they are complements",
                "−2.5; they are complements",
                "0.4; they are substitutes",
                "0.4; they are complements",
                "2.5; they are substitutes",
            ],
            "correct_index": 2,
            "solution": "Cross-price elasticity = (% change in the quantity of good X) / (% change in the price of good Y) = 4% / 10% = 0.4.\n\nIt is positive: when streaming became more expensive, people bought more movie tickets. A positive cross-price elasticity means the goods are substitutes (a negative one would mean complements).\n\n2.5 comes from dividing the wrong way around (10 / 4).",
        },
        {
            "id": "mockf-mc3", "module": "Module 2", "topic": "Elasticity and total revenue",
            "stem": "A climbing-shoe brand sells 10,000 pairs per month at $40 a pair. The price elasticity of demand at this price is −0.6. The brand raises its price to $42.",
            "ask": "Using the elasticity to predict the new quantity, by how much does monthly revenue change?",
            "choices": ["−$12,000", "$0", "$7,400", "$8,000", "$20,000"],
            "correct_index": 2,
            "solution": "Price change: (42 − 40) / 40 = +5%.\nQuantity change: elasticity × %ΔP = −0.6 × 5% = −3%, so the new quantity is 10,000 × 0.97 = 9,700 pairs.\n\nRevenue before: 40 × 10,000 = $400,000.\nRevenue after: 42 × 9,700 = $407,400.\nChange: +$7,400 per month.\n\nDemand is inelastic (|−0.6| < 1), so the price increase raises revenue. ($8,000 is the rough shortcut 5% − 3% = 2% of $400,000; $20,000 forgets that fewer pairs are sold; −$12,000 counts only the lost pairs.)",
        },
        {
            "id": "mockf-mc4", "module": "Module 3", "topic": "Diminishing returns and marginal cost",
            "stem": "A bakery has a fixed number of ovens. Each extra baker it hires adds fewer loaves per hour than the baker before (diminishing marginal product of labor). Every baker earns the same hourly wage, and labor is the only variable input.",
            "ask": "What does this imply for the bakery's short-run costs as it produces more loaves?",
            "choices": [
                "Marginal cost rises with output",
                "Marginal cost falls with output",
                "Marginal cost is constant and equal to the wage",
                "Average fixed cost rises with output",
                "Total cost falls with output",
            ],
            "correct_index": 0,
            "solution": "Marginal cost = wage / marginal product of labor. The wage is constant and each extra baker adds fewer loaves, so each extra loaf needs more labor time than the one before: the cost of an extra loaf goes up.\n\nSo diminishing marginal product means rising marginal cost in the short run.\n\nAverage fixed cost always falls with output (the same fixed cost is spread over more units), and total cost always rises with output.",
        },
        {
            "id": "mockf-mc5", "module": "Module 3", "topic": "Economies of scale",
            "stem": "A battery maker compares two plant sizes, each run in the cheapest possible way (all inputs adjusted, the long run). Producing 1,000 batteries a day costs $50,000 a day in total; producing 2,000 batteries a day costs $80,000 a day in total.",
            "ask": "What does this tell you about the firm's costs over this range of output?",
            "choices": [
                "Diseconomies of scale: the cost per battery rises from $40 to $50",
                "Constant returns to scale: doubling output does not change the cost per battery",
                "Nothing can be said without knowing the fixed costs",
                "Diseconomies of scale: total cost rises from $50,000 to $80,000",
                "Economies of scale: the cost per battery falls from $50 to $40",
            ],
            "correct_index": 4,
            "solution": "Long-run average cost = total cost / quantity.\nAt 1,000 batteries: 50,000 / 1,000 = $50 per battery.\nAt 2,000 batteries: 80,000 / 2,000 = $40 per battery.\n\nThe cost per unit falls as the scale of production grows: economies of scale.\n\nTotal cost always rises with output, so a rise in total cost says nothing about scale. In the long run there are no fixed costs to worry about: all inputs can be adjusted.",
        },
        {
            "id": "mockf-mc6", "module": "Module 4 (Part I)", "topic": "Short-run shutdown decision",
            "stem": "A price-taking firm sells its product at $20. At its best output of 500 units per week, marginal cost is $20, average variable cost is $17 and average total cost is $23. Its fixed costs must be paid this week whether or not it produces.",
            "ask": "What should the firm do this week, and what is its profit or loss?",
            "choices": [
                "Shut down; its loss is $1,500",
                "Shut down; its loss is $3,000",
                "Keep producing; its profit is $1,500",
                "Keep producing; its loss is $4,500",
                "Keep producing; its loss is $1,500",
            ],
            "correct_index": 4,
            "solution": "Fixed cost = (ATC − AVC) × Q = (23 − 17) × 500 = $3,000 per week.\n\nIf it produces: profit = (P − ATC) × Q = (20 − 23) × 500 = −$1,500.\nIf it shuts down: it still pays the fixed cost, so profit = −$3,000.\n\nThe price ($20) is above average variable cost ($17), so every unit sold covers its variable cost and contributes $3 toward the fixed cost. The firm should keep producing in the short run: the loss of $1,500 is smaller than the $3,000 it would lose by shutting down.",
        },
        {
            "id": "mockf-mc7", "module": "Module 4 (Part I)", "topic": "Long-run adjustment in perfect competition",
            "stem": "The market for fresh pasta is perfectly competitive. All firms, current and potential, have the same costs, and input prices do not change as the industry grows. The market starts in long-run equilibrium. Then a popular cooking show permanently raises the demand for fresh pasta.",
            "ask": "Once the market has fully adjusted in the long run, compared with the starting point:",
            "choices": [
                "The price is back at its original level and there are more firms",
                "The price is higher and each firm earns a positive economic profit",
                "The price is higher and the number of firms is unchanged",
                "The price is lower and there are more firms",
                "The price is back at its original level and there are fewer firms",
            ],
            "correct_index": 0,
            "solution": "In the short run, higher demand raises the price, and existing firms earn positive economic profits.\n\nThose profits attract new firms (there are no barriers to entry). Entry shifts the market supply curve to the right and pushes the price down until profits are zero again, which happens when the price is back at the minimum of long-run average cost.\n\nBecause costs are the same for all firms and input prices do not change, that minimum is the same as before: the price returns to its original level, and the larger quantity is produced by more firms.",
        },
        {
            "id": "mockf-mc8", "module": "Module 4 (Part I)", "topic": "Price floor",
            "stem": "In a local market for raw milk, demand is Q = 100 − 2P and supply is Q = 3P − 25, where Q is thousands of liters per week and P is the price in cents per liter. The government sets a minimum price of 30 cents per liter.",
            "ask": "How large is the excess supply (surplus) at the minimum price, in thousands of liters per week?",
            "choices": ["5", "10", "15", "25", "40"],
            "correct_index": 3,
            "solution": "Equilibrium without the floor: 100 − 2P = 3P − 25, so P = 25 cents and Q = 50.\n\nThe minimum price of 30 is above the equilibrium price, so it binds.\nAt P = 30: quantity demanded = 100 − 60 = 40; quantity supplied = 90 − 25 = 65.\n\nExcess supply = 65 − 40 = 25 thousand liters per week. Only 40 are actually sold, 10 fewer than at the equilibrium.",
        },
        {
            "id": "mockf-mc9", "module": "Module 4 (Part I)", "topic": "Who pays a tax",
            "stem": "In the market for gym memberships, demand is Q = 120 − 2P and supply is Q = 4P − 30 (Q in thousands of memberships per month, P in dollars per month). The government introduces a tax of $6 per membership, collected from the gyms.",
            "ask": "By how much does the price paid by consumers rise?",
            "choices": ["$0", "$2", "$3", "$4", "$6"],
            "correct_index": 3,
            "solution": "Before the tax: 120 − 2P = 4P − 30, so P = $25 and Q = 70.\n\nWith the tax, gyms keep only P − 6 of the price consumers pay, so supply becomes Q = 4(P − 6) − 30 = 4P − 54.\nNew equilibrium: 120 − 2P = 4P − 54, so P = $29 and Q = 62.\n\nConsumers pay $29 (up $4); gyms keep 29 − 6 = $23 (down $2). Consumers bear $4 of the $6 tax because demand is less price-sensitive than supply here. Who legally pays the tax does not decide who bears it.",
        },
        {
            "id": "mockf-mc10", "module": "Module 4 (Part II)", "topic": "Negative externality",
            "stem": "A chemical plant sells its product in a competitive market. Its production releases fumes that harm nearby residents, and the plant does not pay for this damage.",
            "ask": "Compared with the efficient outcome, the unregulated market:",
            "choices": [
                "Produces too little, because the plant's private cost is above the social cost",
                "Produces the efficient amount, because the market is competitive",
                "Produces too much, because consumers value the product more than it costs to make",
                "Produces too little, because residents' complaints raise the plant's costs",
                "Produces too much, because the plant's private cost is below the social cost",
            ],
            "correct_index": 4,
            "solution": "With a negative externality, part of the cost of production (the harm to residents) is not paid by the producer. The plant's private marginal cost is below the social marginal cost.\n\nThe market produces where demand meets the private cost curve, which is to the right of where demand meets the social cost curve: too much is produced, and the extra units cost society more than they are worth to buyers (a deadweight loss).\n\nCompetition alone does not fix this, because the price does not include the external cost.",
        },
        {
            "id": "mockf-mc11", "module": "Module 4 (Part II)", "topic": "Corrective (Pigouvian) tax",
            "stem": "In the market for a fertilizer, demand is P = 100 − Q and the private marginal cost of the producers is MC = 20 + Q. Each unit of fertilizer also causes $10 of water pollution downstream, paid by nobody in the market.",
            "ask": "What is the efficient quantity, and what per-unit tax would make the market reach it?",
            "choices": [
                "30 units; a tax of $10 per unit",
                "35 units; a tax of $10 per unit",
                "35 units; a tax of $5 per unit",
                "40 units; no tax is needed",
                "45 units; a subsidy of $10 per unit",
            ],
            "correct_index": 1,
            "solution": "Market outcome: demand = private MC, 100 − Q = 20 + Q, so Q = 40.\n\nEfficient outcome: demand = social MC = private MC + external cost = 30 + Q. So 100 − Q = 30 + Q, and Q = 35.\n\nA tax equal to the external cost, $10 per unit, raises the producers' cost to the social cost, so the market produces 35 units on its own. (Price paid by buyers: 100 − 35 = $65.)",
        },
        {
            "id": "mockf-mc12", "module": "Module 5", "topic": "Markup and the elasticity of demand",
            "stem": "A firm with a patent on a medical device faces a price elasticity of demand of −4 at its profit-maximizing price. Its marginal cost is constant at $30 per device.",
            "ask": "What price is the firm charging?",
            "choices": ["$22.50", "$30.00", "$37.50", "$40.00", "$120.00"],
            "correct_index": 3,
            "solution": "At the profit maximum, MR = MC, and MR = P × (1 + 1/E).\n\nSo P × (1 + 1/(−4)) = 30, which gives P × 0.75 = 30, and P = $40.\n\nThe markup over marginal cost is (40 − 30) / 40 = 25% of the price, which equals 1/|E| = 1/4. The more elastic the demand, the smaller the markup.",
        },
        {
            "id": "mockf-mc13", "module": "Module 5", "topic": "Monopolistic competition in the long run",
            "stem": "Coffee shops in a large city sell slightly different products (location, atmosphere, menu), and new shops can open freely. The market is in long-run equilibrium.",
            "ask": "Which statement describes a typical coffee shop in this equilibrium?",
            "choices": [
                "Its price equals its average total cost, and its price is above its marginal cost",
                "Its price equals its marginal cost, and it earns zero economic profit",
                "Its price is above its average total cost, so it earns a positive economic profit",
                "Its price is below its average total cost, so some shops will leave in the long run",
                "Its price equals its marginal cost, and it produces at the minimum of average total cost",
            ],
            "correct_index": 0,
            "solution": "Each shop faces a downward-sloping demand curve (its product is a bit different), so it sets MR = MC with a price above marginal cost.\n\nFree entry drives economic profit to zero in the long run: new shops open while profits are positive, which reduces each shop's demand until the demand curve just touches the average total cost curve. So P = ATC.\n\nUnlike perfect competition, the shop does not produce at the minimum of ATC and its price is above MC.",
        },
        {
            "id": "mockf-mc14", "module": "Module 5", "topic": "A per-unit tax on a monopolist",
            "stem": "A monopolist faces the inverse demand P = 100 − Q and has a constant marginal cost of $20. The government introduces a tax of $10 on every unit the monopolist sells.",
            "ask": "By how much does the monopolist's profit-maximizing price rise?",
            "choices": ["$0", "$5", "$10", "$15", "$20"],
            "correct_index": 1,
            "solution": "Marginal revenue: MR = 100 − 2Q.\n\nBefore the tax: 100 − 2Q = 20, so Q = 40 and P = 100 − 40 = $60.\nThe tax raises the marginal cost to 20 + 10 = $30: 100 − 2Q = 30, so Q = 35 and P = $65.\n\nThe price rises by $5, only half of the tax. With linear demand and constant marginal cost, the monopolist passes half of a cost increase on to its customers. (A fixed fee, unlike a per-unit tax, would not change the price at all, because it does not change marginal cost.)",
        },
        {
            "id": "mockf-mc15", "module": "Module 6", "topic": "Conditions for price discrimination",
            "stem": "A software company wants to sell the same program at a lower price to university students than to businesses.",
            "ask": "Which set of conditions does the company need for this pricing to work?",
            "choices": [
                "Market power, a way to tell the groups apart, and no resale between them",
                "A perfectly competitive market, so that each group pays a price equal to its marginal cost",
                "The same price elasticity of demand in both groups",
                "Students must have less elastic demand than businesses",
                "A marginal cost that is lower for students than for businesses",
            ],
            "correct_index": 0,
            "solution": "Charging different groups different prices for the same product needs three things:\n1. Market power (a price taker cannot set prices).\n2. A way to identify each group (here, a student ID).\n3. No resale between groups; otherwise businesses would buy cheap copies from students.\n\nThe groups must also differ in their elasticity, and it is the MORE elastic group (students) that gets the lower price. With equal elasticities, the best price would be the same in both groups. The marginal cost of a copy does not need to differ.",
        },
        {
            "id": "mockf-mc16", "module": "Module 6", "topic": "Bundling",
            "stem": "A software firm sells two apps, a photo editor and a video editor, to two customers. Its marginal cost is zero. The most each customer is willing to pay:\n\n  Customer A: photo editor $50, video editor $20\n  Customer B: photo editor $30, video editor $45\n\nThe firm cannot charge different prices to the two customers.",
            "ask": "What is the firm's highest profit if it sells the apps separately, and what is it if it sells only a bundle of both apps?",
            "choices": [
                "Separately $95; bundle $140",
                "Separately $105; bundle $150",
                "Separately $105; bundle $140",
                "Separately $125; bundle $75",
                "Separately $145; bundle $140",
            ],
            "correct_index": 2,
            "solution": "Separately:\nPhoto editor: at $30 both buy, 2 × 30 = $60; at $50 only A buys, $50. Best: $60.\nVideo editor: at $20 both buy, $40; at $45 only B buys, $45. Best: $45.\nTotal: $105.\n\nBundle: A values both apps at 50 + 20 = $70; B at 30 + 45 = $75. At a bundle price of $70 both buy: 2 × 70 = $140 (at $75 only B buys, $75).\n\nThe bundle earns $35 more. It works because the valuations are negatively correlated: the customer who values one app highly values the other less, so the totals are much closer than the separate valuations. ($145 would need each customer to pay their full value for each app, which a single price per app cannot do.)",
        },
        {
            "id": "mockf-mc17", "module": "Module 6", "topic": "Two-part tariff",
            "stem": "A car-wash club sells memberships. Each member's yearly demand for washes is Q = 24 − 2P, where P is the price per wash. The marginal cost of a wash is $4. All members have the same demand. The club charges a yearly membership fee plus a price per wash.",
            "ask": "What is the profit-maximizing yearly membership fee?",
            "choices": ["$16", "$32", "$48", "$64", "$128"],
            "correct_index": 3,
            "solution": "With a two-part tariff and identical customers, set the price per wash equal to marginal cost, $4, and take the whole consumer surplus as the fee.\n\nAt P = 4 each member buys Q = 24 − 8 = 16 washes a year.\nThe demand curve hits the price axis at P = 12 (where Q = 0).\nConsumer surplus = ½ × (12 − 4) × 16 = $64.\n\nSo the fee is $64 per year. ($128 forgets the ½ in the triangle; $16 is the number of washes, not a dollar amount.)",
        },
        {
            "id": "mockf-mc18", "module": "Module 7 (Part I)", "topic": "Bertrand competition",
            "stem": "Two firms sell identical printer cartridges and compete by setting prices at the same time. Customers buy from whichever firm is cheaper (and split equally if prices are equal). Both firms have a constant marginal cost of $10 and no fixed costs, and each can supply the whole market.",
            "ask": "What happens in the Nash equilibrium?",
            "choices": [
                "Both firms charge the monopoly price and share the monopoly profit",
                "Both firms charge a price between $10 and the monopoly price, as in the Cournot model",
                "One firm charges $10 and the other charges the monopoly price",
                "There is no equilibrium, because each firm always wants to undercut the other",
                "Both firms charge $10 and earn zero profit",
            ],
            "correct_index": 4,
            "solution": "If both charged any price above $10, either firm could cut its price by a cent and take the whole market, nearly doubling its profit. So no price above marginal cost can be an equilibrium.\n\nAt P = $10 neither firm can gain: raising the price loses all customers, and cutting it means selling below cost. So both firms charge $10 and earn zero profit, the same price as in perfect competition, even with only two firms.\n\nCournot (quantity competition) gives a price above marginal cost; Bertrand with identical products does not.",
        },
        {
            "id": "mockf-mc19", "module": "Module 7 (Part II)", "topic": "Nash equilibrium",
            "stem": "Two airlines, Alpha and Beta, each decide whether to Add or Skip a new route. Their yearly profits (in $ millions) are:\n\n  Both add: Alpha 20, Beta −10\n  Alpha adds, Beta skips: Alpha 60, Beta 0\n  Alpha skips, Beta adds: Alpha 0, Beta 40\n  Both skip: Alpha 0, Beta 0\n\nThey choose at the same time.",
            "ask": "What is the Nash equilibrium?",
            "choices": [
                "Both add the route",
                "Alpha adds the route and Beta skips it",
                "Alpha skips the route and Beta adds it",
                "Both skip the route",
                "There is no Nash equilibrium in pure strategies",
            ],
            "correct_index": 1,
            "solution": "Alpha: if Beta adds, Add gives 20 and Skip gives 0; if Beta skips, Add gives 60 and Skip gives 0. Adding is better whatever Beta does: a dominant strategy.\n\nBeta: it can expect Alpha to add. Given that, Add gives −10 and Skip gives 0, so Beta skips.\n\nCheck (Add, Skip): Alpha would not switch (60 > 0) and Beta would not switch (0 > −10). It is the only Nash equilibrium: in (Skip, Add) Alpha would switch to Add (20 > 0), and in (Add, Add) Beta would switch to Skip.",
        },
        {
            "id": "mockf-mc20", "module": "Module 8", "topic": "Second-price auction",
            "stem": "Four collectors bid for a vintage poster in a sealed-bid second-price auction: the highest bidder wins and pays the second-highest bid. Their values for the poster are $90, $120, $135 and $150, and each bids in their own best interest.",
            "ask": "How much does the winner pay?",
            "choices": ["$90.00", "$120.00", "$135.00", "$142.50", "$150.00"],
            "correct_index": 2,
            "solution": "In a second-price auction, bidding your true value is a dominant strategy: your bid only decides whether you win, not what you pay, so shading your bid can only make you lose an auction you would have liked to win.\n\nSo the bids equal the values. The collector who values the poster at $150 wins and pays the second-highest bid, $135. (An English auction would end at about the same price: the bidding stops when the $135 bidder drops out.)",
        },
    ],

    # ------------------------------------------------------------------ Part 2
    "problems": [
        {
            "id": "mockf-p1",
            "title": "The island ferry",
            "points": 15,
            "intro": "IslaLink is the only ferry company serving a small island. The daily demand for crossings is Q = 3,000 − 50 × P, where Q is the number of passengers per day and P is the fare in dollars. The marginal cost of carrying a passenger (fuel, cleaning, ticketing) is constant at $12. The company also pays $18,000 per day in fixed costs (crew salaries, the lease of the boat and port fees).",
            "parts": [
                {
                    "id": "mockf-p1a", "label": "(a)", "points": 5,
                    "text": "What fare maximizes IslaLink's profit, and how many passengers does it carry per day at that fare?",
                    "items": [
                        {"id": "mockf-p1a-ans", "kind": "text", "label": "Your answer (inverse demand, marginal revenue, the condition you use, quantity and fare)", "rows": 6},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p1a-r1", "points": 2, "text": "Inverse demand P = 60 − 0.02 × Q and marginal revenue MR = 60 − 0.04 × Q"},
                        {"id": "mockf-p1a-r2", "points": 1, "text": "Uses MR = MC"},
                        {"id": "mockf-p1a-r3", "points": 2, "text": "Q = 1,200 passengers per day and a fare of P = $36"},
                    ],
                    "solution": "Step 1, inverse demand: 50P = 3,000 − Q, so P = 60 − 0.02 × Q.\n\nStep 2, marginal revenue (same intercept, twice the slope): MR = 60 − 0.04 × Q.\n\nStep 3, set MR = MC: 60 − 0.04 × Q = 12, so Q = 48 / 0.04 = 1,200 passengers per day.\n\nStep 4, the fare from the inverse demand: P = 60 − 0.02 × 1,200 = $36.",
                    "figure": {"kind": "dmr", "a": 60, "b": 0.02, "xlabel": "Passengers per day",
                               "points": [{"q": 1200, "p": 36, "label": "P = $36, Q = 1,200"}],
                               "mc": {"value": 12, "label": "MC = $12", "point_label": "MR = MC"}},
                },
                {
                    "id": "mockf-p1b", "label": "(b)", "points": 5,
                    "text": "What is the price elasticity of demand at the profit-maximizing fare? Is demand elastic or inelastic there? Explain why a profit-maximizing firm with a positive marginal cost never sets its price where demand is inelastic.",
                    "items": [
                        {"id": "mockf-p1b-ans", "kind": "text", "label": "Your answer (the elasticity, elastic or inelastic, and the explanation)", "rows": 6},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p1b-r1", "points": 2, "text": "Elasticity = (ΔQ/ΔP) × (P/Q) = −50 × 36 / 1,200 = −1.5"},
                        {"id": "mockf-p1b-r2", "points": 1, "text": "Demand is elastic at this fare (|E| > 1)"},
                        {"id": "mockf-p1b-r3", "points": 2, "text": "Explanation: where demand is inelastic, marginal revenue is negative, so it cannot equal a positive marginal cost (raising the price there would raise revenue and lower costs)"},
                    ],
                    "solution": "Point elasticity: E = (ΔQ/ΔP) × (P/Q). From the demand function, ΔQ/ΔP = −50.\nE = −50 × 36 / 1,200 = −1.5.\n\n|E| = 1.5 > 1, so demand is elastic at the profit-maximizing fare.\n\nWhy this must be so: MR = P × (1 + 1/E). Where demand is inelastic (|E| < 1), MR is negative. A firm with a positive marginal cost needs MR = MC > 0, which is only possible where demand is elastic. Put differently: on the inelastic part, raising the fare would increase revenue (fewer passengers, but a proportionally larger fare) and lower costs (fewer passengers to carry), so profit would rise.\n\nCheck: MR = 36 × (1 − 1/1.5) = 36 × 1/3 = $12 = MC.",
                },
                {
                    "id": "mockf-p1c", "label": "(c)", "points": 5,
                    "text": "What is IslaLink's daily profit at the optimum? The port authority now raises its daily port fee by $4,000 (a fixed amount, paid whatever the number of passengers). What happens to the profit-maximizing fare, the number of passengers and the daily profit? Should IslaLink keep running the ferry?",
                    "items": [
                        {"id": "mockf-p1c-ans", "kind": "text", "label": "Your answer (profit before, then fare, passengers and profit after the fee increase, and whether to keep running)", "rows": 6},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p1c-r1", "points": 2, "text": "Profit = (36 − 12) × 1,200 − 18,000 = $10,800 per day"},
                        {"id": "mockf-p1c-r2", "points": 2, "text": "The fare ($36) and the number of passengers (1,200) do not change, because a fixed fee does not change marginal cost or marginal revenue"},
                        {"id": "mockf-p1c-r3", "points": 1, "text": "Profit falls by the fee, to $6,800 per day; it is still positive, so IslaLink keeps running the ferry"},
                    ],
                    "solution": "Profit = total revenue − variable cost − fixed cost = 36 × 1,200 − 12 × 1,200 − 18,000 = 43,200 − 14,400 − 18,000 = $10,800 per day.\n\nThe higher port fee is a fixed cost: it is paid in full whatever the number of passengers. It does not change marginal revenue or marginal cost, so the condition MR = MC still gives Q = 1,200 and P = $36. Raising the fare to \"pass on\" the fee would only lower profit further.\n\nProfit falls by exactly the fee: 10,800 − 4,000 = $6,800 per day. It is still positive, so IslaLink should keep running the ferry.",
                },
            ],
        },
        {
            "id": "mockf-p2",
            "title": "Lift tickets for tourists and locals",
            "points": 22,
            "intro": "Pine Ridge is the only ski resort in a mountain valley. It sells day lift tickets to two groups. Tourists, who come from far away, have the demand Q_T = 12,000 − 100 × P_T. Local residents have the demand Q_L = 9,000 − 150 × P_L. Quantities are day tickets per season and prices are in dollars per day ticket. The marginal cost of a skier-day (lift operation, grooming, staff) is constant at $15. Ignore fixed costs. To begin with, the resort can tell the two groups apart (locals show a resident ID at the ticket office) and tickets cannot be passed on.",
            "parts": [
                {
                    "id": "mockf-p2a", "label": "(a)", "points": 10,
                    "text": "What are the profit-maximizing price and quantity for tourists and for locals? What is the resort's profit from each group, and its total profit?",
                    "items": [
                        {"id": "mockf-p2a-ans", "kind": "text", "label": "Your answer (for each group: inverse demand, marginal revenue, quantity, price and profit; then the total)", "rows": 8},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p2a-r1", "points": 2, "text": "Sets MR = MC separately for each group"},
                        {"id": "mockf-p2a-r2", "points": 3, "text": "Tourists: MR = 120 − 0.02 × Q_T, so Q_T = 5,250 tickets and P_T = $67.50"},
                        {"id": "mockf-p2a-r3", "points": 3, "text": "Locals: MR = 60 − (1/75) × Q_L, so Q_L = 3,375 tickets and P_L = $37.50"},
                        {"id": "mockf-p2a-r4", "points": 2, "text": "Profits: tourists $275,625, locals $75,937.50, total $351,562.50"},
                    ],
                    "solution": "The groups can be told apart and cannot resell, so the resort sets MR = MC in each group separately.\n\nTourists: inverse demand P_T = 120 − 0.01 × Q_T, so MR_T = 120 − 0.02 × Q_T.\nMR_T = 15 gives Q_T = 105 / 0.02 = 5,250 tickets, and P_T = 120 − 0.01 × 5,250 = $67.50.\nProfit from tourists = (67.50 − 15) × 5,250 = $275,625.\n\nLocals: inverse demand P_L = 60 − Q_L / 150, so MR_L = 60 − Q_L / 75.\nMR_L = 15 gives Q_L = 45 × 75 = 3,375 tickets, and P_L = 60 − 3,375 / 150 = $37.50.\nProfit from locals = (37.50 − 15) × 3,375 = $75,937.50.\n\nTotal profit = 275,625 + 75,937.50 = $351,562.50 per season.",
                },
                {
                    "id": "mockf-p2b", "label": "(b)", "points": 4,
                    "text": "Compute the price elasticity of demand of each group at the prices you found in (a). Use them to explain why one group pays more than the other.",
                    "items": [
                        {"id": "mockf-p2b-ans", "kind": "text", "label": "Your answer (the two elasticities and the explanation)", "rows": 5},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p2b-r1", "points": 1.5, "text": "Tourists: E_T = −100 × 67.50 / 5,250 = −1.29"},
                        {"id": "mockf-p2b-r2", "points": 1.5, "text": "Locals: E_L = −150 × 37.50 / 3,375 = −1.67"},
                        {"id": "mockf-p2b-r3", "points": 1, "text": "Locals have the more elastic demand, so they get the lower price (the markup over marginal cost is smaller where demand is more elastic)"},
                    ],
                    "solution": "Tourists: E_T = (ΔQ/ΔP) × (P/Q) = −100 × 67.50 / 5,250 = −1.29.\nLocals: E_L = −150 × 37.50 / 3,375 = −1.67.\n\nLocals' demand is more elastic: they live nearby, can ski another day or do something else, and react more to the price. The resort charges a lower price to the more price-sensitive group and a higher price to the less price-sensitive one.\n\nCheck with MR = P × (1 + 1/E): tourists 67.50 × (1 − 1/1.29) = 15; locals 37.50 × (1 − 1/1.67) = 15. Both groups have MR equal to the same marginal cost of $15, as they must.",
                },
                {
                    "id": "mockf-p2c", "label": "(c)", "points": 8,
                    "text": "A website starts selling cheap locals' tickets to tourists, so the resort can no longer keep the two prices apart and must charge one price to everyone. What single price maximizes its profit? How many tickets does each group buy at that price, and what is the resort's profit? How much profit does the resort lose compared with (a)?",
                    "items": [
                        {"id": "mockf-p2c-ans", "kind": "text", "label": "Your answer (total demand, marginal revenue, price, tickets per group, profit, and the loss compared with (a))", "rows": 8},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p2c-r1", "points": 2, "text": "Adds the two demands at the same price: Q = 21,000 − 250 × P (valid for prices up to $60, where locals still buy)"},
                        {"id": "mockf-p2c-r2", "points": 2, "text": "P = 84 − 0.004 × Q, MR = 84 − 0.008 × Q = 15, so Q = 8,625 tickets and P = $49.50"},
                        {"id": "mockf-p2c-r3", "points": 1, "text": "Tourists buy 7,050 tickets and locals buy 1,575"},
                        {"id": "mockf-p2c-r4", "points": 2, "text": "Profit = (49.50 − 15) × 8,625 = $297,562.50"},
                        {"id": "mockf-p2c-r5", "points": 1, "text": "The resort loses $54,000 compared with charging two prices"},
                    ],
                    "solution": "With one price, the resort faces the total demand. Add the two demands at the same price (horizontally):\nQ = (12,000 − 100P) + (9,000 − 150P) = 21,000 − 250P.\nThis holds for prices up to $60; above $60 locals buy nothing and only tourists remain.\n\nInverse total demand: P = 84 − 0.004 × Q, so MR = 84 − 0.008 × Q.\nMR = MC: 84 − 0.008 × Q = 15, so Q = 69 / 0.008 = 8,625 tickets, and P = 84 − 0.004 × 8,625 = $49.50.\nThe price is below $60, so both groups do buy, and the total demand used is the right one.\n\nTickets per group: tourists 12,000 − 100 × 49.50 = 7,050; locals 9,000 − 150 × 49.50 = 1,575 (sum 8,625).\n\nProfit = (49.50 − 15) × 8,625 = $297,562.50.\n(The alternative of a high price that only tourists pay gives at most the $275,625 from (a), which is less, so $49.50 is the best single price.)\n\nLoss compared with two prices: 351,562.50 − 297,562.50 = $54,000 per season. Tourists now pay less and locals pay more than in (a). This is why the resort cares about stopping resale.",
                },
            ],
        },
        {
            "id": "mockf-p3",
            "title": "Two cement makers",
            "points": 23,
            "intro": "Two firms, Alpha Cement and Beta Cement, are the only producers in a regional cement market. They sell the same product and compete in quantities (Cournot): each chooses its output at the same time, taking the other's output as given. The market demand is P = 200 − Q, where Q = q_A + q_B is total output in thousands of tons per month and P is the price in dollars per ton. Alpha has a newer plant with a constant marginal cost of $20 per ton; Beta's older plant has a constant marginal cost of $50 per ton. Ignore fixed costs. Profits are in thousands of dollars per month.",
            "parts": [
                {
                    "id": "mockf-p3a", "label": "(a)", "points": 6,
                    "text": "Derive the reaction (best-response) function of each firm.",
                    "items": [
                        {"id": "mockf-p3a-ans", "kind": "text", "label": "Your answer (each firm's residual demand, marginal revenue and reaction function)", "rows": 7},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p3a-r1", "points": 2, "text": "Alpha's marginal revenue given q_B: MR_A = 200 − q_B − 2 × q_A (and the same idea for Beta)"},
                        {"id": "mockf-p3a-r2", "points": 2, "text": "Alpha's reaction function: q_A = 90 − 0.5 × q_B"},
                        {"id": "mockf-p3a-r3", "points": 2, "text": "Beta's reaction function: q_B = 75 − 0.5 × q_A"},
                    ],
                    "solution": "Alpha takes q_B as given and faces the residual demand P = (200 − q_B) − q_A.\nIts revenue is TR_A = (200 − q_B − q_A) × q_A, so MR_A = 200 − q_B − 2 × q_A.\nMR_A = MC_A: 200 − q_B − 2 × q_A = 20, so q_A = 90 − 0.5 × q_B.\n\nBeta in the same way: MR_B = 200 − q_A − 2 × q_B = 50, so q_B = 75 − 0.5 × q_A.\n\nThe two functions are not mirror images: Beta's higher cost makes it produce less for any output of its rival.",
                },
                {
                    "id": "mockf-p3b", "label": "(b)", "points": 7,
                    "text": "Find the Cournot equilibrium: each firm's output, the market price, and each firm's profit.",
                    "items": [
                        {"id": "mockf-p3b-ans", "kind": "text", "label": "Your answer (solve the two reaction functions together; price; each firm's profit)", "rows": 7},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p3b-r1", "points": 3, "text": "q_A = 70 and q_B = 40 (thousand tons per month)"},
                        {"id": "mockf-p3b-r2", "points": 2, "text": "Total output 110 and price P = $90 per ton"},
                        {"id": "mockf-p3b-r3", "points": 2, "text": "Profits: Alpha (90 − 20) × 70 = 4,900; Beta (90 − 50) × 40 = 1,600 (thousand dollars per month)"},
                    ],
                    "solution": "Substitute Beta's reaction function into Alpha's:\nq_A = 90 − 0.5 × (75 − 0.5 × q_A) = 52.5 + 0.25 × q_A, so 0.75 × q_A = 52.5 and q_A = 70.\nThen q_B = 75 − 0.5 × 70 = 40.\n\nTotal output Q = 110 thousand tons, and P = 200 − 110 = $90 per ton.\n\nProfits (thousand dollars per month):\nAlpha: (90 − 20) × 70 = 4,900.\nBeta: (90 − 50) × 40 = 1,600.\n\nThe low-cost firm produces more and earns much more, but both price above their marginal costs.",
                },
                {
                    "id": "mockf-p3c", "label": "(c)", "points": 6,
                    "text": "Alpha proposes to buy Beta. After the merger, the combined firm is a monopoly and makes all its cement in Alpha's cheaper plant (which has enough capacity). Find the merged firm's output, price and profit. By how much does the two firms' combined profit rise compared with (b)?",
                    "items": [
                        {"id": "mockf-p3c-ans", "kind": "text", "label": "Your answer (output, price, profit of the merged firm, and the change in combined profit)", "rows": 6},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p3c-r1", "points": 1, "text": "Uses the monopoly condition MR = 200 − 2 × Q = 20 (the low marginal cost)"},
                        {"id": "mockf-p3c-r2", "points": 2, "text": "Q = 90 thousand tons and P = $110 per ton"},
                        {"id": "mockf-p3c-r3", "points": 2, "text": "Profit = (110 − 20) × 90 = 8,100 (thousand dollars per month)"},
                        {"id": "mockf-p3c-r4", "points": 1, "text": "Combined profit rises by 8,100 − (4,900 + 1,600) = 1,600"},
                    ],
                    "solution": "The merged firm is a monopoly with marginal cost $20 (it uses only the cheaper plant).\nMR = 200 − 2 × Q = 20, so Q = 90 thousand tons per month, and P = 200 − 90 = $110 per ton.\nProfit = (110 − 20) × 90 = 8,100 thousand dollars per month.\n\nBefore the merger the two firms earned 4,900 + 1,600 = 6,500 together, so combined profit rises by 1,600 per month.\n\nTwo things raise profit: the merged firm restricts total output (from 110 to 90) and raises the price, and it moves all production to the cheaper plant. Since the merger adds 3,200 to Alpha's own profit (8,100 − 4,900) and Beta earns 1,600 on its own, any purchase price between 1,600 and 3,200 per month of profit would leave both owners better off.",
                },
                {
                    "id": "mockf-p3d", "label": "(d)", "points": 4,
                    "text": "Compute consumer surplus before the merger (part b) and after it (part c). Why might the competition authority want to block the merger, even though it moves production to the cheaper plant?",
                    "items": [
                        {"id": "mockf-p3d-ans", "kind": "text", "label": "Your answer (consumer surplus before and after, and the argument)", "rows": 5},
                    ],
                    "self_rubric": [
                        {"id": "mockf-p3d-r1", "points": 1, "text": "Before: CS = ½ × (200 − 90) × 110 = 6,050"},
                        {"id": "mockf-p3d-r2", "points": 1, "text": "After: CS = ½ × (200 − 110) × 90 = 4,050 (a fall of 2,000)"},
                        {"id": "mockf-p3d-r3", "points": 2, "text": "Argument: price rises and output falls; consumers lose more (2,000) than the firms gain (1,600), so total surplus falls by 400"},
                    ],
                    "solution": "Consumer surplus is the triangle under the demand curve and above the price (demand hits the price axis at $200).\n\nBefore: CS = ½ × (200 − 90) × 110 = 6,050 thousand dollars per month.\nAfter: CS = ½ × (200 − 110) × 90 = 4,050. Consumers lose 2,000.\n\nThe merger raises the price from $90 to $110 and cuts output from 110 to 90 thousand tons. Consumers lose 2,000 while the firms gain only 1,600, so total surplus falls by 400 per month (6,050 + 6,500 = 12,550 before; 4,050 + 8,100 = 12,150 after). The cost saving from using the better plant is not large enough to offset the harm from the loss of competition, which is why the authority might block the merger.",
                },
            ],
        },
    ],
}
