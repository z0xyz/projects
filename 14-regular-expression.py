import re

rdRegexProject = re.compile(r"\[info\] Writing video subtitles to: (.*).en.vtt\n\[download\] Downloading video \d of \d*\n\[youtube\] -?\w*: Downloading webpage\n(\[youtube\] \w*: Downloading MPD manifest)?")
matchObject = rdRegexProject.findall(
'''
[info] Writing video subtitles to: Introduction to Mathematics-JbhBdOfMEPs.en.vtt
[download] Downloading video 2 of 165
[youtube] rV7WjNWHOsI: Downloading webpage
[youtube] rV7WjNWHOsI: Downloading MPD manifest

[info] Writing video subtitles to: Addition and Subtraction of Small Numbers-rV7WjNWHOsI.en.vtt
[download] Downloading video 3 of 165
[youtube] fr04p6Ar9ic: Downloading webpage
[youtube] fr04p6Ar9ic: Downloading MPD manifest

[info] Writing video subtitles to: Multiplication and Division of Small Numbers-fr04p6Ar9ic.en.vtt
[download] Downloading video 4 of 165
[youtube] qyW2mWvvtZ8: Downloading webpage
[youtube] qyW2mWvvtZ8: Downloading MPD manifest

[info] Writing video subtitles to: Understanding Fractions, Improper Fractions, and Mixed Numbers-qyW2mWvvtZ8.en.vtt
[download] Downloading video 5 of 165
[youtube] AkWtUOwlUgs: Downloading webpage
[youtube] AkWtUOwlUgs: Downloading MPD manifest

[info] Writing video subtitles to: Large Whole Numbers - Place Values and Estimating-AkWtUOwlUgs.en.vtt
[download] Downloading video 6 of 165
[youtube] jC4SWFag6Qw: Downloading webpage

[info] Writing video subtitles to: Decimals - Notation and Operations-jC4SWFag6Qw.en.vtt
[download] Downloading video 7 of 165
[youtube] n9fgcm0Pwgs: Downloading webpage
[youtube] n9fgcm0Pwgs: Downloading MPD manifest

[info] Writing video subtitles to: Working With Percentages-n9fgcm0Pwgs.en.vtt
[download] Downloading video 8 of 165
[youtube] -Xt4UDk7Kzw: Downloading webpage

[info] Writing video subtitles to: Converting Between Fractions, Decimals, and Percentages--Xt4UDk7Kzw.en.vtt
[download] Downloading video 9 of 165
[youtube] YFyOsvnr9ig: Downloading webpage
[youtube] YFyOsvnr9ig: Downloading MPD manifest

[info] Writing video subtitles to: Addition and Subtraction of Large Numbers-YFyOsvnr9ig.en.vtt
[download] Downloading video 10 of 165
[youtube] LC_R2Zh66fU: Downloading webpage
[youtube] LC_R2Zh66fU: Downloading MPD manifest

[info] Writing video subtitles to: The Distributive Property for Arithmetic-LC_R2Zh66fU.en.vtt
[download] Downloading video 11 of 165
[youtube] s1Ly3cX4yHc: Downloading webpage
[info] Writing video subtitles to: Multiplication of Large Numbers-s1Ly3cX4yHc.en.vtt
[download] Downloading video 12 of 165
[youtube] rI2peJT2Ty8: Downloading webpage
[info] Writing video subtitles to: Division of Large Numbers - Long Division-rI2peJT2Ty8.en.vtt
[download] Downloading video 13 of 165
[youtube] 3-5DKCLJspM: Downloading webpage
[youtube] 3-5DKCLJspM: Downloading MPD manifest
[info] Writing video subtitles to: Negative Numbers-3-5DKCLJspM.en.vtt
[download] Downloading video 14 of 165
[youtube] K_TD9GuP9uQ: Downloading webpage
[youtube] K_TD9GuP9uQ: Downloading MPD manifest
[info] Writing video subtitles to: Understanding Exponents and Their Operations-K_TD9GuP9uQ.en.vtt
[download] Downloading video 15 of 165
[youtube] y_f7c3ztFrI: Downloading webpage
[youtube] y_f7c3ztFrI: Downloading MPD manifest
[info] Writing video subtitles to: Order of Arithmetic Operations - PEMDAS-y_f7c3ztFrI.en.vtt
[download] Downloading video 16 of 165
[youtube] WZWKJG9fxnU: Downloading webpage
[youtube] WZWKJG9fxnU: Downloading MPD manifest
[info] Writing video subtitles to: Divisibility, Prime Numbers, and Prime Factorization-WZWKJG9fxnU.en.vtt
[download] Downloading video 17 of 165
[youtube] sae1IoToQ0M: Downloading webpage
[youtube] sae1IoToQ0M: Downloading MPD manifest
[info] Writing video subtitles to: Least Common Multiple (LCM)-sae1IoToQ0M.en.vtt
[download] Downloading video 18 of 165
[youtube] GFmdqe4z9zU: Downloading webpage
[info] Writing video subtitles to: Greatest Common Factor (GCF)-GFmdqe4z9zU.en.vtt
[download] Downloading video 19 of 165
[youtube] -ijpdtjDNZw: Downloading webpage
[info] Writing video subtitles to: Addition and Subtraction of Fractions--ijpdtjDNZw.en.vtt
[download] Downloading video 20 of 165
[youtube] Q9MCRjrrd6E: Downloading webpage
[youtube] Q9MCRjrrd6E: Downloading MPD manifest
[info] Writing video subtitles to: Multiplication and Division of Fractions-Q9MCRjrrd6E.en.vtt
[download] Downloading video 21 of 165
[youtube] FM7Q2yVLZIc: Downloading webpage
[info] Writing video subtitles to: Analyzing Sets of Data - Range, Mean, Median, and Mode-FM7Q2yVLZIc.en.vtt
[download] Downloading video 22 of 165
[youtube] WZdZhuUSmpM: Downloading webpage
[youtube] WZdZhuUSmpM: Downloading MPD manifest
[info] Writing video subtitles to: Introduction to Algebra - Using Variables-WZdZhuUSmpM.en.vtt
[download] Downloading video 23 of 165
[youtube] 0bZ2GcCTtCA: Downloading webpage
[info] Writing video subtitles to: Basic Number Properties for Algebra-0bZ2GcCTtCA.en.vtt
[download] Downloading video 24 of 165
[youtube] 2mnQ3t02Tss: Downloading webpage
[youtube] 2mnQ3t02Tss: Downloading MPD manifest
[info] Writing video subtitles to: Algebraic Equations and Their Solutions-2mnQ3t02Tss.en.vtt
[download] Downloading video 25 of 165
[youtube] aJ0abU348ds: Downloading webpage
[youtube] aJ0abU348ds: Downloading MPD manifest
[info] Writing video subtitles to: Algebraic Equations With Variables on Both Sides-aJ0abU348ds.en.vtt
[download] Downloading video 26 of 165
[youtube] jOJLfQq9ktw: Downloading webpage
[youtube] jOJLfQq9ktw: Downloading MPD manifest
[info] Writing video subtitles to: Algebraic Word Problems-jOJLfQq9ktw.en.vtt
[download] Downloading video 27 of 165
[youtube] uBxs7cSgOes: Downloading webpage
[youtube] uBxs7cSgOes: Downloading MPD manifest
[info] Writing video subtitles to: Solving Algebraic Inequalities-uBxs7cSgOes.en.vtt
[download] Downloading video 28 of 165
[youtube] 7vomY6g-f3Q: Downloading webpage
[info] Writing video subtitles to: Square Roots, Cube Roots, and Other Roots-7vomY6g-f3Q.en.vtt
[download] Downloading video 29 of 165
[youtube] OAIctPYiMrw: Downloading webpage
[youtube] OAIctPYiMrw: Downloading MPD manifest
[info] Writing video subtitles to: Simplifying Expressions With Roots and Exponents-OAIctPYiMrw.en.vtt
[download] Downloading video 30 of 165
[youtube] EnJuHTq0ni0: Downloading webpage
[youtube] EnJuHTq0ni0: Downloading MPD manifest
[info] Writing video subtitles to: Solving Algebraic Equations With Roots and Exponents-EnJuHTq0ni0.en.vtt
[download] Downloading video 31 of 165
[youtube] nPPNgin7W7Y: Downloading webpage
[youtube] nPPNgin7W7Y: Downloading MPD manifest
[info] Writing video subtitles to: Introduction to Polynomials-nPPNgin7W7Y.en.vtt
[download] Downloading video 32 of 165
[youtube] 0aJBtUOXpsk: Downloading webpage
[youtube] 0aJBtUOXpsk: Downloading MPD manifest
[info] Writing video subtitles to: Adding and Subtracting Polynomials-0aJBtUOXpsk.en.vtt
[download] Downloading video 33 of 165
[youtube] RTC7RIwdZcE: Downloading webpage
[info] Writing video subtitles to: Multiplying Binomials by the FOIL Method-RTC7RIwdZcE.en.vtt
[download] Downloading video 34 of 165
[youtube] GuwofNeT9ok: Downloading webpage
[youtube] GuwofNeT9ok: Downloading MPD manifest
[info] Writing video subtitles to: Solving Quadratics by Factoring-GuwofNeT9ok.en.vtt
[download] Downloading video 35 of 165
[youtube] P8W2M0jq2Qs: Downloading webpage
[info] Writing video subtitles to: Solving Quadratics by Completing the Square-P8W2M0jq2Qs.en.vtt
[download] Downloading video 36 of 165
[youtube] UTuxHsaH-gQ: Downloading webpage
[youtube] UTuxHsaH-gQ: Downloading MPD manifest
[info] Writing video subtitles to: Solving Quadratics by Using the Quadratic Formula-UTuxHsaH-gQ.en.vtt
[download] Downloading video 37 of 165
[youtube] WRkgMDVIETE: Downloading webpage
[info] Writing video subtitles to: Solving Higher Degree Polynomials by Synthetic Division and the Rational Roots Test-WRkgMDVIETE.en.vtt
[download] Downloading video 38 of 165
[youtube] KfrkcGx2Xl8: Downloading webpage
[youtube] KfrkcGx2Xl8: Downloading MPD manifest
[info] Writing video subtitles to: Manipulating Rational Expressions - Simplification and Operations-KfrkcGx2Xl8.en.vtt
[download] Downloading video 39 of 165
[youtube] ntzgiu7Ta0s: Downloading webpage
[youtube] ntzgiu7Ta0s: Downloading MPD manifest
[info] Writing video subtitles to: Graphing in Algebra - Ordered Pairs and the Coordinate Plane-ntzgiu7Ta0s.en.vtt
[download] Downloading video 40 of 165
[youtube] lz8zVJxRFX8: Downloading webpage
[info] Writing video subtitles to: Graphing Lines in Algebra - Understanding Slopes and Y-Intercepts-lz8zVJxRFX8.en.vtt
[download] Downloading video 41 of 165
[youtube] T-acWVybQtk: Downloading webpage
[youtube] T-acWVybQtk: Downloading MPD manifest
[info] Writing video subtitles to: Graphing Lines in Slope-Intercept Form (y = mx + b)-T-acWVybQtk.en.vtt
[download] Downloading video 42 of 165
[youtube] -DnmoFnQUtk: Downloading webpage
[info] Writing video subtitles to: Graphing Lines in Standard Form (ax + by = c)--DnmoFnQUtk.en.vtt
[download] Downloading video 43 of 165
[youtube] 0oe-GqFrYFU: Downloading webpage
[youtube] 0oe-GqFrYFU: Downloading MPD manifest
[info] Writing video subtitles to: Graphing Parallel and Perpendicular Lines-0oe-GqFrYFU.en.vtt
[download] Downloading video 44 of 165
[youtube] 2DzmE3_QS-E: Downloading webpage
[info] Writing video subtitles to: Solving Systems of Two Equations and Two Unknowns - Graphing, Substitution, and Elimination-2DzmE3_QS-E.en.vtt
[download] Downloading video 45 of 165
[youtube] Wirk4o3FHPA: Downloading webpage
[youtube] Wirk4o3FHPA: Downloading MPD manifest
[info] Writing video subtitles to: Absolute Values - Defining, Calculating, and Graphing-Wirk4o3FHPA.en.vtt
[download] Downloading video 46 of 165
[youtube] QUGmwPwtbpg: Downloading webpage
[info] Writing video subtitles to: What are the Types of Numbers Real vs. Imaginary, Rational vs. Irrational-QUGmwPwtbpg.en.vtt
[download] Downloading video 47 of 165
[youtube] THtc8pDU7J8: Downloading webpage
[youtube] THtc8pDU7J8: Downloading MPD manifest
[info] Writing video subtitles to: Introduction to Geometry - Ancient Greece and the Pythagoreans-THtc8pDU7J8.en.vtt
[download] Downloading video 48 of 165
[youtube] JHMB_ob89qs: Downloading webpage
[youtube] JHMB_ob89qs: Downloading MPD manifest
[info] Writing video subtitles to: Basic Euclidean Geometry - Points, Lines, and Planes-JHMB_ob89qs.en.vtt
[download] Downloading video 49 of 165
[youtube] dA94zyaLuhk: Downloading webpage
[info] Writing video subtitles to: Types of Angles and Angle Relationships-dA94zyaLuhk.en.vtt
[download] Downloading video 50 of 165
[youtube] lQ5AuNVjxhI: Downloading webpage
[youtube] lQ5AuNVjxhI: Downloading MPD manifest
[info] Writing video subtitles to: Types of Triangles in Euclidean Geometry-lQ5AuNVjxhI.en.vtt
[download] Downloading video 51 of 165
[youtube] mJ4Ms6SXEgg: Downloading webpage
[youtube] mJ4Ms6SXEgg: Downloading MPD manifest
[info] Writing video subtitles to: Proving Triangle Congruence and Similarity-mJ4Ms6SXEgg.en.vtt
[download] Downloading video 52 of 165
[youtube] ByWrUSKHTGc: Downloading webpage
[youtube] ByWrUSKHTGc: Downloading MPD manifest
[info] Writing video subtitles to: Special Lines in Triangles - Bisectors, Medians, and Altitudes-ByWrUSKHTGc.en.vtt
[download] Downloading video 53 of 165
[youtube] ojMemmYifxM: Downloading webpage
[info] Writing video subtitles to: The Triangle Midsegment Theorem-ojMemmYifxM.en.vtt
[download] Downloading video 54 of 165
[youtube] 37PX8DV_b9Y: Downloading webpage
[youtube] 37PX8DV_b9Y: Downloading MPD manifest
[info] Writing video subtitles to: The Pythagorean Theorem-37PX8DV_b9Y.en.vtt
[download] Downloading video 55 of 165
[youtube] jTZs8bRoWxE: Downloading webpage
[info] Writing video subtitles to: Types of Quadrilaterals and Other Polygons-jTZs8bRoWxE.en.vtt
[download] Downloading video 56 of 165
[youtube] J11IU3C86Yc: Downloading webpage
[youtube] J11IU3C86Yc: Downloading MPD manifest
[info] Writing video subtitles to: Calculating the Perimeter of Polygons-J11IU3C86Yc.en.vtt
[download] Downloading video 57 of 165
[youtube] SBIv5-7RbQY: Downloading webpage
[youtube] SBIv5-7RbQY: Downloading MPD manifest
[info] Writing video subtitles to: Circles - Radius, Diameter, Chords, Circumference, and Sectors-SBIv5-7RbQY.en.vtt
[download] Downloading video 58 of 165
[youtube] _zzV2DV19IU: Downloading webpage
[info] Writing video subtitles to: Calculating the Area of Shapes-_zzV2DV19IU.en.vtt
[download] Downloading video 59 of 165
[youtube] VjI4LtotC2o: Downloading webpage
[youtube] VjI4LtotC2o: Downloading MPD manifest
[info] Writing video subtitles to: Proving the Pythagorean Theorem-VjI4LtotC2o.en.vtt
[download] Downloading video 60 of 165
[youtube] sAd3Eo25Bbg: Downloading webpage
[youtube] sAd3Eo25Bbg: Downloading MPD manifest
[info] Writing video subtitles to: Three-Dimensional Shapes Part 1 - Types, Calculating Surface Area-sAd3Eo25Bbg.en.vtt
[download] Downloading video 61 of 165
[youtube] CI-G9_bTKuw: Downloading webpage
[youtube] CI-G9_bTKuw: Downloading MPD manifest
[info] Writing video subtitles to: Three-Dimensional Shapes Part 2 - Calculating Volume-CI-G9_bTKuw.en.vtt
[download] Downloading video 62 of 165
[youtube] LmudKHXSMp4: Downloading webpage
[info] Writing video subtitles to: Back to Algebra - What are Functions-LmudKHXSMp4.en.vtt
[download] Downloading video 63 of 165
[youtube] q3zmcFvHxP4: Downloading webpage
[youtube] q3zmcFvHxP4: Downloading MPD manifest
[info] Writing video subtitles to: Manipulating Functions Algebraically and Evaluating Composite Functions-q3zmcFvHxP4.en.vtt
[download] Downloading video 64 of 165
[youtube] EjsQWKq-dGQ: Downloading webpage
[info] Writing video subtitles to: Graphing Algebraic Functions - Domain and Range, Maxima and Minima-EjsQWKq-dGQ.en.vtt
[download] Downloading video 65 of 165
[youtube] MkP1LJR2PyM: Downloading webpage
[info] Writing video subtitles to: Transforming Algebraic Functions - Shifting, Stretching, and Reflecting-MkP1LJR2PyM.en.vtt
[download] Downloading video 66 of 165
[youtube] BIQrnx-vvx8: Downloading webpage
[info] Writing video subtitles to: Continuous, Discontinuous, and Piecewise Functions-BIQrnx-vvx8.en.vtt
[download] Downloading video 67 of 165
[youtube] 9fJsrnE1go0: Downloading webpage
[info] Writing video subtitles to: Inverse Functions-9fJsrnE1go0.en.vtt
[download] Downloading video 68 of 165
[youtube] wzQstigxbuo: Downloading webpage
[info] Writing video subtitles to: The Distance Formula - Finding the Distance Between Two Points-wzQstigxbuo.en.vtt
[download] Downloading video 69 of 165
[youtube] JUvo3GrgWHk: Downloading webpage
[info] Writing video subtitles to: Graphing Conic Sections Part 1 - Circles-JUvo3GrgWHk.en.vtt
[download] Downloading video 70 of 165
[youtube] iwRlllkqADw: Downloading webpage
[youtube] iwRlllkqADw: Downloading MPD manifest
[info] Writing video subtitles to: Graphing Conic Sections Part 2 - Ellipses-iwRlllkqADw.en.vtt
[download] Downloading video 71 of 165
[youtube] hvJkCMzFiX8: Downloading webpage
[youtube] hvJkCMzFiX8: Downloading MPD manifest
[info] Writing video subtitles to: Graphing Conic Sections Part 3 - Parabolas in Standard Form-hvJkCMzFiX8.en.vtt
[download] Downloading video 72 of 165
[youtube] h5aVROOmI-Q: Downloading webpage
[youtube] h5aVROOmI-Q: Downloading MPD manifest
[info] Writing video subtitles to: Graphing Conic Sections Part 4 - Hyperbolas-h5aVROOmI-Q.en.vtt
[download] Downloading video 73 of 165
[youtube] CHEtGgTexHI: Downloading webpage
[info] Writing video subtitles to: Graphing Higher-Degree Polynomials - The Leading Coefficient Test and Finding Zeros-CHEtGgTexHI.en.vtt
[download] Downloading video 74 of 165
[youtube] fy45qX8cUwQ: Downloading webpage
[info] Writing video subtitles to: Graphing Rational Functions and Their Asymptotes-fy45qX8cUwQ.en.vtt
[download] Downloading video 75 of 165
[youtube] Es37gGo5F4Y: Downloading webpage
[youtube] Es37gGo5F4Y: Downloading MPD manifest
[info] Writing video subtitles to: Solving and Graphing Polynomial and Rational Inequalities-Es37gGo5F4Y.en.vtt
[download] Downloading video 76 of 165
[youtube] tAaDItpC8OI: Downloading webpage
[info] Writing video subtitles to: Evaluating and Graphing Exponential Functions-tAaDItpC8OI.en.vtt
[download] Downloading video 77 of 165
[youtube] 1Yv4fEsGpvM: Downloading webpage
[info] Writing video subtitles to: Logarithms Part 1 - Evaluation of Logs and Graphing Logarithmic Functions-1Yv4fEsGpvM.en.vtt
[download] Downloading video 78 of 165
[youtube] sQ2ix7QcGwQ: Downloading webpage
[info] Writing video subtitles to: Logarithms Part 2 - Base Ten Logs, Natural Logs, and the Change-Of-Base Property-sQ2ix7QcGwQ.en.vtt
[download] Downloading video 79 of 165
[youtube] MSTSBW8LPRM: Downloading webpage
[info] Writing video subtitles to: Logarithms Part 3 - Properties of Logs, Expanding Logarithmic Expressions-MSTSBW8LPRM.en.vtt
[download] Downloading video 80 of 165
[youtube] 10I_TVuYLkQ: Downloading webpage
[info] Writing video subtitles to: Solving Exponential and Logarithmic Equations-10I_TVuYLkQ.en.vtt
[download] Downloading video 81 of 165
[youtube] Yddjxj49C_M: Downloading webpage
[info] Writing video subtitles to: Complex Numbers - Operations, Complex Conjugates, and the Linear Factorization Theorem-Yddjxj49C_M.en.vtt
[download] Downloading video 82 of 165
[youtube] 6JkCmZAQaio: Downloading webpage
[info] Writing video subtitles to: Set Theory - Types of Sets, Unions and Intersections-6JkCmZAQaio.en.vtt
[download] Downloading video 83 of 165
[youtube] -DPkqpmm1sI: Downloading webpage
[info] Writing video subtitles to: Sequences, Factorials, and Summation Notation--DPkqpmm1sI.en.vtt
[download] Downloading video 84 of 165
[youtube] 0ZsSRx0o0zE: Downloading webpage
[info] Writing video subtitles to: Theoretical Probability, Permutations and Combinations-0ZsSRx0o0zE.en.vtt
[download] Downloading video 85 of 165
[youtube] 0GkmnPdD6jY: Downloading webpage
[info] Writing video subtitles to: Introduction to Trigonometry - Angles and Radians-0GkmnPdD6jY.en.vtt
[download] Downloading video 86 of 165
[youtube] cqIZue-plBI: Downloading webpage
[info] Writing video subtitles to: Trigonometric Functions - Sine, Cosine, Tangent, Cosecant, Secant, and Cotangent-cqIZue-plBI.en.vtt
[download] Downloading video 87 of 165
[youtube] 75dMcyCUo2g: Downloading webpage
[info] Writing video subtitles to: The Easiest Way to Memorize the Trigonometric Unit Circle-75dMcyCUo2g.en.vtt
[download] Downloading video 88 of 165
[youtube] Ql7ducUjiG0: Downloading webpage
[info] Writing video subtitles to: Basic Trigonometric Identities - Pythagorean Identities and Cofunction Identities-Ql7ducUjiG0.en.vtt
[download] Downloading video 89 of 165
[youtube] 8oEjxGjAeQI: Downloading webpage
[info] Writing video subtitles to: Graphing Trigonometric Functions-8oEjxGjAeQI.en.vtt
[download] Downloading video 90 of 165
[youtube] YXWKpgmLgHk: Downloading webpage
[info] Writing video subtitles to: Inverse Trigonometric Functions-YXWKpgmLgHk.en.vtt
[download] Downloading video 91 of 165
[youtube] YYKGkYkKeMM: Downloading webpage
[info] Writing video subtitles to: Verifying Trigonometric Identities-YYKGkYkKeMM.en.vtt
[download] Downloading video 92 of 165
[youtube] 0cB4MLhaCk0: Downloading webpage
[info] Writing video subtitles to: Formulas for Trigonometric Functions - Sum_Difference, Double_Half-Angle, Prod-to-Sum_Sum-to-Prod-0cB4MLhaCk0.en.vtt
[download] Downloading video 93 of 165
[youtube] aq4b24jcZOc: Downloading webpage
[info] Writing video subtitles to: Solving Trigonometric Equations-aq4b24jcZOc.en.vtt
[download] Downloading video 94 of 165
[youtube] MmfO1YgzmHI: Downloading webpage
[info] Writing video subtitles to: The Law of Sines-MmfO1YgzmHI.en.vtt
[download] Downloading video 95 of 165
[youtube] 3wGQMyaWoLA: Downloading webpage
[info] Writing video subtitles to: The Law of Cosines-3wGQMyaWoLA.en.vtt
[download] Downloading video 96 of 165
[youtube] jwLUapqnwkk: Downloading webpage
[info] Writing video subtitles to: Polar Coordinates and Graphing Polar Equations-jwLUapqnwkk.en.vtt
[download] Downloading video 97 of 165
[youtube] QaN_3TytT_U: Downloading webpage
[info] Writing video subtitles to: Parametric Equations-QaN_3TytT_U.en.vtt
[download] Downloading video 98 of 165
[youtube] rBVi_9qAKTU: Downloading webpage
[info] Writing video subtitles to: Introduction to Calculus - The Greeks, Newton, and Leibniz-rBVi_9qAKTU.en.vtt
[download] Downloading video 99 of 165
[youtube] ktOYbZ8CpLA: Downloading webpage
[info] Writing video subtitles to: Understanding Differentiation Part 1 - The Slope of a Tangent Line-ktOYbZ8CpLA.en.vtt
[download] Downloading video 100 of 165
[youtube] J27BZCX1OF8: Downloading webpage
[youtube] J27BZCX1OF8: Downloading MPD manifest
[info] Writing video subtitles to: Understanding Differentiation Part 2 - Rates of Change-J27BZCX1OF8.en.vtt
[download] Downloading video 101 of 165
[youtube] wK8WuTEc0ns: Downloading webpage
[info] Writing video subtitles to: Limits and Limit Laws in Calculus-wK8WuTEc0ns.en.vtt
[download] Downloading video 102 of 165
[youtube] x3iEEDxrhyE: Downloading webpage
[info] Writing video subtitles to: What is a Derivative Deriving the Power Rule-x3iEEDxrhyE.en.vtt
[download] Downloading video 103 of 165
[youtube] aL15O6rS9z0: Downloading webpage
[youtube] aL15O6rS9z0: Downloading MPD manifest
[info] Writing video subtitles to: Derivatives of Polynomial Functions - Power Rule, Product Rule, and Quotient Rule-aL15O6rS9z0.en.vtt
[download] Downloading video 104 of 165
[youtube] _Zqcxbjzyxg: Downloading webpage
[info] Writing video subtitles to: Derivatives of Trigonometric Functions-_Zqcxbjzyxg.en.vtt
[download] Downloading video 105 of 165
[youtube] _x1nCg2LfuA: Downloading webpage
[youtube] _x1nCg2LfuA: Downloading MPD manifest
[info] Writing video subtitles to: Derivatives of Composite Functions - The Chain Rule-_x1nCg2LfuA.en.vtt
[download] Downloading video 106 of 165
[youtube] zjKMkbcbtHY: Downloading webpage
[info] Writing video subtitles to: Derivatives of Logarithmic and Exponential Functions-zjKMkbcbtHY.en.vtt
[download] Downloading video 107 of 165
[youtube] M0SMSWM2oZA: Downloading webpage
[info] Writing video subtitles to: Implicit Differentiation-M0SMSWM2oZA.en.vtt
[download] Downloading video 108 of 165
[youtube] zUDxgehxQqs: Downloading webpage
[info] Writing video subtitles to: Higher Derivatives and Their Applications-zUDxgehxQqs.en.vtt
[download] Downloading video 109 of 165
[youtube] j6I3EXiKB2A: Downloading webpage
[info] Writing video subtitles to: Related Rates in Calculus-j6I3EXiKB2A.en.vtt
[download] Downloading video 110 of 165
[youtube] pvLj1s7SOtk: Downloading webpage
[info] Writing video subtitles to: Finding Local Maxima and Minima by Differentiation-pvLj1s7SOtk.en.vtt
[download] Downloading video 111 of 165
[youtube] dIY86WqvGjw: Downloading webpage
[info] Writing video subtitles to: Graphing Functions and Their Derivatives-dIY86WqvGjw.en.vtt
[download] Downloading video 112 of 165
[youtube] q1U6AmIa_uQ: Downloading webpage
[info] Writing video subtitles to: Optimization Problems in Calculus-q1U6AmIa_uQ.en.vtt
[download] Downloading video 113 of 165
[youtube] g45quDrSA6g: Downloading webpage
[info] Writing video subtitles to: Understanding Limits and L'Hospital's Rule-g45quDrSA6g.en.vtt
[download] Downloading video 114 of 165
[youtube] FsC3do74UIo: Downloading webpage
[info] Writing video subtitles to: What is Integration Finding the Area Under a Curve-FsC3do74UIo.en.vtt
[download] Downloading video 115 of 165
[youtube] NLU9U8-wJrM: Downloading webpage
[info] Writing video subtitles to: The Fundamental Theorem of Calculus - Redefining Integration-NLU9U8-wJrM.en.vtt
[download] Downloading video 116 of 165
[youtube] b0RJkIBhfEM: Downloading webpage
[info] Writing video subtitles to: Properties of Integrals and Evaluating Definite Integrals-b0RJkIBhfEM.en.vtt
[download] Downloading video 117 of 165
[youtube] -xHA2RjVkwY: Downloading webpage
[info] Writing video subtitles to: Evaluating Indefinite Integrals--xHA2RjVkwY.en.vtt
[download] Downloading video 118 of 165
[youtube] 7bJXbDqi9FE: Downloading webpage
[youtube] 7bJXbDqi9FE: Downloading MPD manifest
[info] Writing video subtitles to: Evaluating Integrals With Trigonometric Functions-7bJXbDqi9FE.en.vtt
[download] Downloading video 119 of 165
[youtube] sci1pls4Lc8: Downloading webpage
[info] Writing video subtitles to: Integration Using The Substitution Rule-sci1pls4Lc8.en.vtt
[download] Downloading video 120 of 165
[youtube] zNU8iK8sGD0: Downloading webpage
[info] Writing video subtitles to: Integration By Parts-zNU8iK8sGD0.en.vtt
[download] Downloading video 121 of 165
[youtube] t3rzxSgvZZk: Downloading webpage
[youtube] t3rzxSgvZZk: Downloading MPD manifest
[info] Writing video subtitles to: Integration by Trigonometric Substitution-t3rzxSgvZZk.en.vtt
[download] Downloading video 122 of 165
[youtube] 8APOcBqbG-U: Downloading webpage
[youtube] 8APOcBqbG-U: Downloading MPD manifest
[info] Writing video subtitles to: Advanced Strategy for Integration in Calculus-8APOcBqbG-U.en.vtt
[download] Downloading video 123 of 165
[youtube] 0JOIhPfXnxc: Downloading webpage
[youtube] 0JOIhPfXnxc: Downloading MPD manifest
[info] Writing video subtitles to: Evaluating Improper Integrals-0JOIhPfXnxc.en.vtt
[download] Downloading video 124 of 165
[youtube] xec6HTcn2M8: Downloading webpage
[youtube] xec6HTcn2M8: Downloading MPD manifest
[info] Writing video subtitles to: Finding the Area Between Two Curves by Integration-xec6HTcn2M8.en.vtt
[download] Downloading video 125 of 165
[youtube] QLHJl2_aM5Q: Downloading webpage
[info] Writing video subtitles to: Calculating the Volume of a Solid of Revolution by Integration-QLHJl2_aM5Q.en.vtt
[download] Downloading video 126 of 165
[youtube] MNU5DT-CDrc: Downloading webpage
[youtube] MNU5DT-CDrc: Downloading MPD manifest
[info] Writing video subtitles to: Calculating Volume by Cylindrical Shells-MNU5DT-CDrc.en.vtt
[download] Downloading video 127 of 165
[youtube] 56-JCZIkDVU: Downloading webpage
[info] Writing video subtitles to: The Mean Value Theorem For Integrals - Average Value of a Function-56-JCZIkDVU.en.vtt
[download] Downloading video 128 of 165
[youtube] L-JqHo4-W4k: Downloading webpage
[youtube] L-JqHo4-W4k: Downloading MPD manifest
[info] Writing video subtitles to: Convergence and Divergence - The Return of Sequences and Series-L-JqHo4-W4k.en.vtt
[download] Downloading video 129 of 165
[youtube] Jtnxi9uM7yA: Downloading webpage
[info] Writing video subtitles to: Estimating Sums Using the Integral Test and Comparison Test-Jtnxi9uM7yA.en.vtt
[download] Downloading video 130 of 165
[youtube] -Md4CEW0-zM: Downloading webpage
[youtube] -Md4CEW0-zM: Downloading MPD manifest
[info] Writing video subtitles to: Alternating Series, Types of Convergence, and The Ratio Test--Md4CEW0-zM.en.vtt
[download] Downloading video 131 of 165
[youtube] OxVBT83x8oc: Downloading webpage
[info] Writing video subtitles to: Power Series-OxVBT83x8oc.en.vtt
[download] Downloading video 132 of 165
[youtube] a58otkmkHtk: Downloading webpage
[info] Writing video subtitles to: Taylor and Maclaurin Series-a58otkmkHtk.en.vtt
[download] Downloading video 133 of 165
[youtube] uMXcKY_w3w4: Downloading webpage
[info] Writing video subtitles to: Hyperbolic Functions - Definitions, Identities, Derivatives, and Inverses-uMXcKY_w3w4.en.vtt
[download] Downloading video 134 of 165
[youtube] 5sJdfciNM20: Downloading webpage
[info] Writing video subtitles to: Three-Dimensional Coordinates and the Right-Hand Rule-5sJdfciNM20.en.vtt
[download] Downloading video 135 of 165
[youtube] KBSCMTYaH1s: Downloading webpage
[info] Writing video subtitles to: Introduction to Vectors and Their Operations-KBSCMTYaH1s.en.vtt
[download] Downloading video 136 of 165
[youtube] 0iNrGpwZwog: Downloading webpage
[info] Writing video subtitles to: The Vector Dot Product-0iNrGpwZwog.en.vtt
[download] Downloading video 137 of 165
[youtube] csgNflj69-Y: Downloading webpage
[info] Writing video subtitles to: Introduction to Linear Algebra - Systems of Linear Equations-csgNflj69-Y.en.vtt
[download] Downloading video 138 of 165
[youtube] y6bVhgmy2rw: Downloading webpage
[info] Writing video subtitles to: Understanding Matrices and Matrix Notation-y6bVhgmy2rw.en.vtt
[download] Downloading video 139 of 165
[youtube] T2Gtt8WygiU: Downloading webpage
[info] Writing video subtitles to: Manipulating Matrices - Elementary Row Operations and Gauss-Jordan Elimination-T2Gtt8WygiU.en.vtt
[download] Downloading video 140 of 165
[youtube] biyQzy2yRUA: Downloading webpage
[info] Writing video subtitles to: Types of Matrices and Matrix Addition-biyQzy2yRUA.en.vtt
[download] Downloading video 141 of 165
[youtube] P5GJJ02OG08: Downloading webpage
[info] Writing video subtitles to: Matrix Multiplication and Associated Properties-P5GJJ02OG08.en.vtt
[download] Downloading video 142 of 165
[youtube] CcbyMH3Noow: Downloading webpage
[info] Writing video subtitles to: Evaluating the Determinant of a Matrix-CcbyMH3Noow.en.vtt
[download] Downloading video 143 of 165
[youtube] gPnWm-IXoAY: Downloading webpage
[info] Writing video subtitles to: The Vector Cross Product-gPnWm-IXoAY.en.vtt
[download] Downloading video 144 of 165
[youtube] kWorj5BBy9k: Downloading webpage
[info] Writing video subtitles to: Inverse Matrices and Their Properties-kWorj5BBy9k.en.vtt
[download] Downloading video 145 of 165
[youtube] RdLo-9jh2EM: Downloading webpage
[youtube] RdLo-9jh2EM: Downloading MPD manifest
[info] Writing video subtitles to: Solving Systems Using Cramer's Rule-RdLo-9jh2EM.en.vtt
[download] Downloading video 146 of 165
[youtube] EP2ghkO0lSk: Downloading webpage
[info] Writing video subtitles to: Understanding Vector Spaces-EP2ghkO0lSk.en.vtt
[download] Downloading video 147 of 165
[youtube] tM4TDL9Hj8U: Downloading webpage
[info] Writing video subtitles to: Subspaces and Span-tM4TDL9Hj8U.en.vtt
[download] Downloading video 148 of 165
[youtube] 9kDpbZCK62Y: Downloading webpage
[info] Writing video subtitles to: Linear Independence-9kDpbZCK62Y.en.vtt
[download] Downloading video 149 of 165
[youtube] 4C9GKyfUQkc: Downloading webpage
[info] Writing video subtitles to: Basis and Dimension-4C9GKyfUQkc.en.vtt
[download] Downloading video 150 of 165
[youtube] HZa1RwFHgwU: Downloading webpage
[info] Writing video subtitles to: Change of Basis-HZa1RwFHgwU.en.vtt
[download] Downloading video 151 of 165
[youtube] is1cg5yhdds: Downloading webpage
[info] Writing video subtitles to: Linear Transformations on Vector Spaces-is1cg5yhdds.en.vtt
[download] Downloading video 152 of 165
[youtube] vyYrvhbDhW4: Downloading webpage
[youtube] vyYrvhbDhW4: Downloading MPD manifest
[info] Writing video subtitles to: Image and Kernel-vyYrvhbDhW4.en.vtt
[download] Downloading video 153 of 165
[youtube] 6nqMegdbxik: Downloading webpage
[info] Writing video subtitles to: Orthogonality and Orthonormality-6nqMegdbxik.en.vtt
[download] Downloading video 154 of 165
[youtube] zHbfZWZJTGc: Downloading webpage
[youtube] zHbfZWZJTGc: Downloading MPD manifest
[info] Writing video subtitles to: The Gram-Schmidt Process-zHbfZWZJTGc.en.vtt
[download] Downloading video 155 of 165
[youtube] TQvxWaQnrqI: Downloading webpage
[info] Writing video subtitles to: Finding Eigenvalues and Eigenvectors-TQvxWaQnrqI.en.vtt
[download] Downloading video 156 of 165
[youtube] WTLl03D4TNA: Downloading webpage
[info] Writing video subtitles to: Diagonalization-WTLl03D4TNA.en.vtt
[download] Downloading video 157 of 165
[youtube] DUuTx2nbizM: Downloading webpage
[info] Writing video subtitles to: Complex, Hermitian, and Unitary Matrices-DUuTx2nbizM.en.vtt
[download] Downloading video 158 of 165
[youtube] UubU3U2C8WM: Downloading webpage
[info] Writing video subtitles to: Double and Triple Integrals-UubU3U2C8WM.en.vtt
[download] Downloading video 159 of 165
[youtube] AXH9Xm6Rbfc: Downloading webpage
[info] Writing video subtitles to: Partial Derivatives and the Gradient of a Function-AXH9Xm6Rbfc.en.vtt
[download] Downloading video 160 of 165
[youtube] 2qxxd68fZng: Downloading webpage
[info] Writing video subtitles to: Vector Fields, Divergence, and Curl-2qxxd68fZng.en.vtt
[download] Downloading video 161 of 165
[youtube] Tz14rC0XvHI: Downloading webpage
[info] Writing video subtitles to: Evaluating Line Integrals-Tz14rC0XvHI.en.vtt
[download] Downloading video 162 of 165
[youtube] kdTxN4E0vbo: Downloading webpage
[info] Writing video subtitles to: Green's Theorem-kdTxN4E0vbo.en.vtt
[download] Downloading video 163 of 165
[youtube] Gml1HT4y3_c: Downloading webpage
[youtube] Gml1HT4y3_c: Downloading MPD manifest
[info] Writing video subtitles to: Evaluating Surface Integrals-Gml1HT4y3_c.en.vtt
[download] Downloading video 164 of 165
[youtube] QS-zUSu-nxA: Downloading webpage
[info] Writing video subtitles to: Stokes's Theorem-QS-zUSu-nxA.en.vtt
[download] Downloading video 165 of 165
[youtube] vZGvgru4TwE: Downloading webpage
[info] Writing video subtitles to: The Divergence Theorem-vZGvgru4TwE.en.vtt
[download] Finished downloading playlist: Mathematics (All Of It)
''')


if type(matchObject) != type(None):
	for item in matchObject:
		print(item)
