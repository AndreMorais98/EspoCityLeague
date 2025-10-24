# ⚛️ Espo City League Frontend

<div align="center">

**React + TypeScript Frontend for Espo City League Football Prediction Platform**

[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![SCSS](https://img.shields.io/badge/SCSS-CC6699?style=for-the-badge&logo=sass&logoColor=white)](https://sass-lang.com/)

</div>

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [🌐 API Integration](#-api-integration)
- [🎨 Styling](#-styling)
- [📄 License](#-license)

## 🎯 Overview

The Espo City League frontend is a modern, responsive React application built with TypeScript that provides an intuitive interface for football prediction management. It features a collapsible sidebar, real-time updates, and a beautiful dark theme.

### 🌟 Key Features

- **React 18**: Latest React features with hooks and concurrent rendering
- **TypeScript**: Full type safety and enhanced developer experience
- **Responsive Design**: Mobile-first approach with collapsible sidebar
- **Mobile Sidebar**: Full-screen mobile sidebar with toggle button
- **Dark Theme**: Professional dark theme with smooth animations
- **Real-time Updates**: Live match results and leaderboard updates
- **Advanced Leaderboard**: Tie-breaking system with detailed statistics
- **Admin Dashboard**: Comprehensive admin interface for match management
- **Context API**: Efficient state management with React Context
- **SCSS Styling**: Modular and maintainable stylesheets

## 🏗️ Architecture

```
frontend/
├── public/              # Static assets
│   ├── images/         # Images and icons
│   └── index.html      # HTML template
├── src/
│   ├── components/     # Reusable UI components
│   │   ├── Sidebar/    # Navigation sidebar
│   │   ├── MatchCard/  # Match display component
│   │   └── ProtectedRoute/ # Route protection
│   ├── pages/          # Page components
│   │   ├── Home/       # Main layout
│   │   ├── Games/      # My Predictions page
│   │   ├── OthersBets/ # Community predictions
│   │   ├── Leaderboard/# Rankings page
│   │   ├── AdminMatches/ # Admin match management (admin)
│   │   ├── CreateMatch/ # Create new matches (admin)
│   │   └── Login/      # Authentication page
│   ├── contexts/       # React Context providers
│   │   ├── UserContext.tsx    # User state management
│   │   └── SidebarContext.tsx # Sidebar state management
│   ├── services/       # API service layer
│   │   ├── api.ts      # HTTP client and API calls
│   │   └── auth.ts     # Authentication service
│   ├── utils/          # Utility functions
│   │   └── stageUtils.ts # Stage analysis utilities
│   ├── routes/         # Routing configuration
│   │   └── AppRouter.tsx # Main router setup
│   ├── styles/         # Global styles
│   │   └── globals.scss # Global CSS variables and styles
│   ├── App.tsx         # Main App component
│   └── main.tsx        # Application entry point
├── package.json        # Dependencies and scripts
└── tsconfig.json       # TypeScript configuration
```

## 🚀 Quick Start

### Prerequisites
- Node.js 16+
- npm or yarn
- Backend API running (see [Backend README](../backend/README.md))

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/espo-city-league.git
cd espo-city-league/frontend

# Install dependencies
npm install
# or
yarn install
```

### 2. Environment Setup
```bash
# Create environment file
cp .env.example .env.local

# Edit .env.local with your API URL
REACT_APP_API_URL=http://localhost:8000/api
```

### 3. Start Development Server
```bash
# Start development server
npm start
# or
yarn start

# The app will open at http://localhost:3000
```

### 4. Build for Production
```bash
# Build the application
npm run build
# or
yarn build

# Serve production build locally
npx serve -s build
# or
yarn global add serve && serve -s build
```

### 5. Live Application
- **Production URL**: [https://espocity-league.mooo.com](https://espocity-league.mooo.com)
- **Login Page**: [https://espocity-league.mooo.com/login](https://espocity-league.mooo.com/login)

## 🏆 Advanced Features

### Mobile Sidebar
- **Full-Screen Mobile**: On mobile devices (≤768px), sidebar takes full screen
- **Toggle Button**: Hamburger menu button (☰) for easy access
- **Smooth Animations**: Slide-in/out transitions with overlay
- **Touch-Friendly**: Optimized for mobile interaction

### Advanced Leaderboard
- **Tie-Breaking System**: Sophisticated ranking when scores are tied
- **Visual Statistics**: Color-coded tie-breaking metrics
- **Hover Tooltips**: Explanatory tooltips for each statistic
- **Real-time Updates**: Automatic updates when match results change

#### Tie-Breaking Metrics
1. **✓ Correct Results**: Exact score predictions (green)
2. **🐺 Lone Wolf Victories**: Unique correct predictions (orange/white)
3. **✗ Defeats**: Games with 0 points (red)

### Smart Navigation
- **Auto-Scroll to Upcoming**: All stage-based pages automatically scroll to upcoming stage
- **Chronological Order**: Maintains proper stage order while showing upcoming first
- **Consistent Behavior**: Same scrollbar behavior across Games, Community Predictions, and Admin pages
- **Smooth Animation**: Elegant scrolling transitions

### Admin Features
- **Match Management**: Edit match results with automatic score recalculation
- **Create Matches**: Full match creation interface with team and stage selection
- **Statistics Update**: Manual tie-breaking statistics refresh
- **Smart Carousel**: Stages carousel scrolls to upcoming stage
- **Real-time Sync**: Changes reflect immediately across the platform

### Match Creation Interface
- **Team Selection**: Dropdown with all available teams
- **Validation**: Prevents same team for home/away
- **Stage Selection**: Dropdown with all stages
- **Date/Time Picker**: Native datetime-local input for kickoff
- **Venue Field**: Optional text field for match location
- **Form Validation**: Comprehensive error handling and success messages
- **Admin Only**: Access restricted to superusers

### Performance Optimizations
- **Duplicate Call Prevention**: useRef-based loading state management
- **Efficient API Calls**: Prevents unnecessary duplicate requests
- **React StrictMode Compatible**: Works correctly in development mode
- **Error Recovery**: Smart retry mechanism on API failures

## 🎨 Styling

### SCSS Architecture
- **Global Variables**: CSS custom properties for theming
- **Component Styles**: Scoped styles for each component
- **Responsive Design**: Mobile-first approach
- **Dark Theme**: Professional dark color scheme

### CSS Variables
```scss
:root {
  // Colors
  --primary-color: #2196F3;
  --primary-hover-color: #1976D2;
  --background-color: #0f172a;
  --surface-color: #1e293b;
  --text-color: #ffffff;
  --text-muted: #94a3b8;
  
  // Spacing
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  // Border radius
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 12px;
}
```

### Responsive Design
```scss
// Mobile-first responsive design
.component {
  padding: var(--spacing-md);
  
  @media (min-width: 768px) {
    padding: var(--spacing-lg);
  }
  
  @media (min-width: 1024px) {
    padding: var(--spacing-xl);
  }
}
```

### Environment Variables
```bash
# .env.local
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_APP_NAME=Espo City League
REACT_APP_VERSION=1.0.0
```

**Note**: The API URL should include the `/api` prefix as all backend endpoints are now prefixed with `/api`.


## 📚 Additional Resources

- [React Documentation](https://reactjs.org/docs/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Create React App Documentation](https://create-react-app.dev/)
- [React Router Documentation](https://reactrouter.com/)
- [SCSS Documentation](https://sass-lang.com/documentation)


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
