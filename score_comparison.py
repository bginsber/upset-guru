from sleeper_wrapper import League, Stats
import pandas as pd
from typing import Dict, List, Tuple
from sleeper_wrapper import Players

class ScoreComparison:
    def __init__(self, league_id: str):
        self.league = League(league_id)
        self.stats = Stats()
        self.players = Players()
        # Get league settings to determine scoring type
        self.league_data = self.league.get_league()
        self.scoring_type = self._determine_scoring_type()
        print(f"\nLeague scoring type detected: {self.scoring_type}")
        
    def _determine_scoring_type(self) -> str:
        """Determine the scoring type based on league settings"""
        settings = self.league_data.get('scoring_settings', {})
        # Check if league uses PPR scoring
        rec_point = float(settings.get('rec', 0))
        if rec_point == 1.0:
            return "pts_ppr"
        elif rec_point == 0.5:
            return "pts_half_ppr"
        else:
            return "pts_std"
            
    def get_team_names(self) -> Dict:
        """Get mapping of roster IDs to team names"""
        rosters = self.league.get_rosters()
        users = self.league.get_users()
        roster_id_to_owner = self.league.map_rosterid_to_ownerid(rosters)
        user_to_team = self.league.map_users_to_team_name(users)
        
        roster_to_team = {}
        for roster_id, owner_id in roster_id_to_owner.items():
            if owner_id:
                roster_to_team[roster_id] = user_to_team.get(owner_id, f"Team {roster_id}")
            else:
                roster_to_team[roster_id] = f"Team {roster_id}"
        return roster_to_team

    def calculate_team_score(self, starters: List[str], stats_data: Dict, is_projections: bool = False) -> Tuple[float, List[Dict]]:
        """Calculate total score for a team's starters and return player details"""
        total_score = 0
        score_type = self.scoring_type
        player_details = []
        
        # Get all player data
        all_players = self.players.get_all_players()
        
        for player_id in starters:
            player_score = 0
            player_name = all_players.get(player_id, {}).get('full_name', player_id)
            position = all_players.get(player_id, {}).get('position', 'Unknown')
            
            if player_id in stats_data:
                player_stats = stats_data[player_id]
                if score_type in player_stats:
                    player_score = float(player_stats[score_type] or 0)
                    total_score += player_score
            
            player_details.append({
                'name': player_name,
                'position': position,
                'score': player_score
            })
                
        return round(total_score, 2), player_details

    def get_weekly_comparison(self, week: int, season: int = 2024) -> List[Dict]:
        """Get projected vs actual scores for all teams in a given week"""
        print(f"\nAnalyzing Week {week} of {season} Season")
        
        # Get team name mappings
        roster_to_team = self.get_team_names()
        
        # Get matchups for the week
        matchups = self.league.get_matchups(week)
        if not matchups:
            print(f"No matchups found for Week {week}")
            return []
            
        # Get projections and actual stats
        projections = self.stats.get_week_projections("regular", season, week)
        actual_stats = self.stats.get_week_stats("regular", season, week)
        
        if not projections:
            print("Warning: No projection data available")
        if not actual_stats:
            print("Warning: No actual stats data available")
        
        results = []
        for matchup in matchups:
            roster_id = matchup["roster_id"]
            starters = matchup["starters"]
            team_name = roster_to_team.get(roster_id, f"Team {roster_id}")
            
            print(f"\nTeam: {team_name}")
            print("=" * 50)
            
            # Calculate projected scores with player details
            projected_score, projected_details = self.calculate_team_score(starters, projections, is_projections=True)
            print("\nProjected Lineup:")
            print("-" * 40)
            for player in projected_details:
                print(f"{player['position']:3} {player['name']:<25} {player['score']:.2f}")
            print(f"{'Total':29} {projected_score:.2f}")
            
            # Calculate actual scores with player details
            actual_score, actual_details = self.calculate_team_score(starters, actual_stats, is_projections=False)
            print("\nActual Lineup:")
            print("-" * 40)
            for player in actual_details:
                print(f"{player['position']:3} {player['name']:<25} {player['score']:.2f}")
            print(f"{'Total':29} {actual_score:.2f}")
            
            results.append({
                "team_name": team_name,
                "projected_score": projected_score,
                "actual_score": actual_score,
                "difference": round(actual_score - projected_score, 2)
            })
            
        return results

def main():
    # Your league ID
    LEAGUE_ID = "1115763150936297472"
    SEASON = 2024
    
    score_comparison = ScoreComparison(LEAGUE_ID)
    
    # Get comparison for a specific week
    week = 1  # Change this to the week you want to analyze
    results = score_comparison.get_weekly_comparison(week)
    
    # Convert to pandas DataFrame for nice display
    df = pd.DataFrame(results)
    df = df.sort_values("difference", ascending=False)
    
    print("\nSummary:")
    print("=" * 60)
    print(df.to_string(index=False))

if __name__ == "__main__":
    main() 