# Fantasy Football Performance Tracker

A simple web interface to track and analyze fantasy football team performance versus projections throughout the season.

## Features

- Overall performance summary for all teams
- Detailed weekly performance breakdown for each team
- Visual indicators for over/under performance
- Responsive design that works on both desktop and mobile devices

## Setup for GitHub Pages

1. Create a new repository on GitHub
2. Clone this repository to your local machine
3. Copy all files (`index.html`, `styles.css`, `script.js`) to your repository
4. Commit and push the changes to GitHub
5. Go to your repository settings on GitHub
6. Under "GitHub Pages", select the main branch as the source
7. Your site will be available at `https://<username>.github.io/<repository-name>`

## Local Development

To run the site locally:

1. Clone the repository
2. Open `index.html` in your web browser
3. No server required - it's all client-side!

## Data Structure

The weekly scores data is stored in `script.js` in the following format:

```javascript
{
    "Team Name": {
        week_number: [actual_score, projected_score],
        // ... more weeks
    },
    // ... more teams
}
```

## Contributing

Feel free to submit issues and enhancement requests! 