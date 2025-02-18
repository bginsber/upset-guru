"""
Weekly scores and projections data for the 2024 season.
Format: (actual_score, projected_score)
"""

WEEKLY_SCORES = {
    "From the 2000s": {
        1: (104.62, 107.84),
        2: (140.28, 113.36),
        3: (146.18, 115.15),
        4: (111.54, 113.62),
        5: (115.12, 108.85),
        6: (117.92, 104.95),
        7: (117.14, 112.55),
        8: (135.96, 105.86),
        9: (140.50, 115.90),  # Week 9 actual score added
        10: (130.80, 117.75),
        11: (147.08, 110.24),
        12: (135.68, 112.30),
        13: (162.88, 118.71),
        14: (112.50, 95.18)
    },
    "Gibbing you a Scare": {
        1: (98.86, 100.60),
        2: (87.92, 109.85),
        3: (84.86, 104.08),
        4: (143.22, 100.83),
        5: (148.22, 100.87),
        6: (124.76, 107.76),
        7: (132.34, 111.50),
        8: (140.94, 117.71),
        9: (123.16, 116.46),  # Week 9 actual score added
        10: (88.78, 104.51),
        11: (91.44, 110.03),
        12: (159.70, 116.54),
        13: (120.24, 114.98),
        14: (143.36, 112.25)
    },
    "Love? AJ Don't Hurts Me": {
        1: (122.92, 113.58),
        2: (129.52, 105.11),
        3: (91.64, 102.58),
        4: (96.42, 104.89),
        5: (78.46, 97.73),
        6: (146.16, 98.43),
        7: (143.16, 115.09),
        8: (142.34, 113.97),
        9: (110.08, 122.43),  # Week 9 actual score added
        10: (119.58, 121.80),
        11: (126.34, 119.39),
        12: (102.46, 119.07),
        13: (106.42, 117.98),
        14: (152.62, 111.50)
    },
    "London Calling": {
        1: (99.58, 110.92),
        2: (105.56, 111.24),
        3: (118.38, 110.21),
        4: (83.12, 105.11),
        5: (101.76, 96.43),
        6: (91.90, 107.04),
        7: (123.68, 101.12),
        8: (68.70, 104.99),
        9: (97.18, 98.73),  # Week 9 actual score added
        10: (75.74, 104.20),
        11: (113.52, 102.04),
        12: (119.88, 99.02),
        13: (91.50, 103.13),
        14: (94.14, 97.92)
    },
    "Team gsalitan": {
        1: (74.84, 94.96),
        2: (58.20, 91.33),
        3: (96.14, 97.36),
        4: (103.32, 93.36),
        5: (103.40, 86.55),
        6: (101.10, 92.93),
        7: (89.10, 85.50),
        8: (92.20, 81.44),
        9: (88.60, 85.30),  # Week 9 actual score added
        10: (90.22, 88.53),
        11: (68.36, 80.71),
        12: (72.36, 71.64),
        13: (69.40, 80.73),
        14: (77.70, 68.61)
    },
    "Rookie Award or Bust": {
        1: (48.46, 101.62),
        2: (102.90, 100.68),
        3: (121.46, 99.24),
        4: (132.10, 99.36),
        5: (161.64, 93.56),
        6: (113.42, 101.93),
        7: (62.14, 84.12),
        8: (137.98, 106.73),
        9: (85.34, 101.86),  # Week 9 actual score added
        10: (142.12, 103.48),
        11: (142.74, 100.04),
        12: (84.28, 89.36),
        13: (129.16, 103.58),
        14: (124.96, 104.69)
    },
    "Kyren in the Club": {
        1: (110.18, 107.08),
        2: (159.14, 110.34),
        3: (128.38, 110.88),
        4: (73.98, 112.26),
        5: (120.70, 105.62),
        6: (97.06, 100.69),
        7: (139.40, 111.01),
        8: (128.88, 108.34),
        9: (92.56, 109.35),  # Week 9 actual score added
        10: (100.74, 110.35),
        11: (119.40, 106.33),
        12: (87.00, 102.24),
        13: (106.30, 116.07),
        14: (133.26, 108.07)
    },
    "Karma is my TE": {
        1: (103.04, 103.07),
        2: (72.34, 107.13),
        3: (116.88, 99.32),
        4: (114.00, 101.22),
        5: (73.44, 86.80),
        6: (85.20, 91.34),
        7: (61.56, 97.56),
        8: (112.26, 100.30),
        9: (112.54, 89.88),  # Week 9 actual score added
        10: (96.94, 100.55),
        11: (70.54, 99.66),
        12: (67.86, 91.74),
        13: (125.64, 100.10),
        14: (35.90, 71.27)
    },
    "Mazal": {
        1: (109.22, 103.84),
        2: (129.90, 103.25),
        3: (116.56, 105.21),
        4: (131.58, 97.60),
        5: (128.76, 90.10),
        6: (108.10, 98.51),
        7: (105.30, 103.51),
        8: (89.70, 103.36),
        9: (165.80, 106.35),  # Week 9 actual score added
        10: (97.94, 112.64),
        11: (126.98, 102.67),
        12: (108.26, 93.10),
        13: (131.94, 104.57),
        14: (128.68, 102.64)
    },
    "Shit Team": {
        1: (155.08, 108.21),
        2: (129.36, 100.68),
        3: (74.22, 107.76),
        4: (81.20, 101.80),
        5: (117.14, 101.63),
        6: (84.20, 94.13),
        7: (85.32, 107.04),
        8: (117.14, 110.57),
        9: (156.00, 118.87),  # Week 9 actual score added
        10: (119.30, 115.54),
        11: (140.98, 111.98),
        12: (97.56, 104.73),
        13: (125.72, 111.12),
        14: (183.48, 115.30)
    }
}

def get_team_scores(team_name: str, week: int) -> tuple:
    """
    Get a team's actual and projected scores for a specific week.
    Returns tuple of (actual_score, projected_score)
    """
    return WEEKLY_SCORES.get(team_name, {}).get(week, (None, None))

def get_weekly_scores(week: int) -> dict:
    """
    Get all teams' actual and projected scores for a specific week.
    Returns dict of team_name: (actual_score, projected_score)
    """
    return {team: scores.get(week, (None, None)) 
            for team, scores in WEEKLY_SCORES.items()}

def get_team_all_weeks(team_name: str) -> dict:
    """
    Get all weekly scores for a specific team.
    Returns dict of week: (actual_score, projected_score)
    """
    return WEEKLY_SCORES.get(team_name, {}) 

results = []
for team, weeks in WEEKLY_SCORES.items():
    total_diff = 0
    count = 0
    weekly_diffs = []
    
    for week, (actual, projected) in weeks.items():
        if actual is not None and projected is not None:
            diff = actual - projected
            total_diff += diff
            weekly_diffs.append(diff)
            count += 1
    
    avg_diff = total_diff / count if count > 0 else 0
    max_overperform = max(weekly_diffs) if weekly_diffs else 0
    min_underperform = min(weekly_diffs) if weekly_diffs else 0
    
    results.append({
        'team': team,
        'avg_diff': round(avg_diff, 2),
        'max_overperform': round(max_overperform, 2),
        'min_underperform': round(min_underperform, 2),
        'weeks_over_projected': sum(1 for d in weekly_diffs if d > 0)
    })

# Sort by average difference in descending order
results.sort(key=lambda x: x['avg_diff'], reverse=True)

print("\nTeam Performance vs Projections (Sorted by Average Points Above Projection):")
print("=" * 100)
print(f"{'Team':<25} {'Avg +/-':<10} {'Best Week +/-':<15} {'Worst Week +/-':<15} {'Weeks Over Projected'}")
print("-" * 100)
for r in results:
    print(f"{r['team']:<25} {r['avg_diff']:>7.2f}    {r['max_overperform']:>8.2f}        {r['min_underperform']:>8.2f}        {r['weeks_over_projected']}/14") 