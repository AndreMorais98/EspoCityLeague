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
- [📁 Project Structure](#-project-structure)
- [🌐 API Integration](#-api-integration)
- [🎨 Styling](#-styling)
- [📄 License](#-license)

## 🎯 Overview

The Espo City League frontend is a modern, responsive React application built with TypeScript that provides an intuitive interface for football prediction management. It features a collapsible sidebar, real-time updates, and a beautiful dark theme.

### 🌟 Key Features

- **React 18**: Latest React features with hooks and concurrent rendering
- **TypeScript**: Full type safety and enhanced developer experience
- **Responsive Design**: Mobile-first approach with collapsible sidebar
- **Dark Theme**: Professional dark theme with smooth animations
- **Real-time Updates**: Live match results and leaderboard updates
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
│   │   ├── AdminMatches/ # Admin match management
│   │   └── Login/      # Authentication page
│   ├── contexts/       # React Context providers
│   │   ├── UserContext.tsx    # User state management
│   │   └── SidebarContext.tsx # Sidebar state management
│   ├── services/       # API service layer
│   │   └── api.ts      # HTTP client and API calls
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

## 📁 Project Structure

### Components (`src/components/`)

#### Sidebar Component
- **Collapsible Navigation**: Toggle between full and icon-only mode
- **User Profile**: Display user info and logout functionality
- **Admin Access**: Conditional admin menu items
- **Smooth Animations**: CSS transitions for collapse/expand

#### MatchCard Component
- **Prediction Interface**: Create and edit match predictions
- **Real-time Status**: Live match indicators and results
- **Validation**: Input validation and error handling
- **Responsive Design**: Mobile-optimized layout

#### ProtectedRoute Component
- **Authentication Guard**: Protect routes requiring login
- **Redirect Logic**: Automatic redirect to login page
- **User Context**: Access to current user state

### Pages (`src/pages/`)

#### Home Page
- **Layout Container**: Main application layout
- **Sidebar Integration**: Responsive sidebar with context
- **Outlet Rendering**: Child route rendering

#### Games Page (My Predictions)
- **Stage Navigation**: Tabbed interface for different matchdays
- **Match Display**: Grid of match cards with predictions
- **Smart Selection**: Automatic upcoming stage selection
- **Visual Indicators**: Past/upcoming stage styling

#### OthersBets Page
- **Community View**: See other users' predictions
- **Match Grouping**: Predictions grouped by match
- **User Display**: Show prediction authors
- **Stage Navigation**: Same smart stage selection

#### AdminMatches Page
- **Admin Only**: Restricted to superuser accounts
- **Match Management**: Update match scores and results
- **Real-time Updates**: Immediate score updates
- **Validation**: Input validation for scores

#### Leaderboard Page
- **Rankings Display**: User rankings with points
- **Performance Metrics**: Win/loss statistics
- **Visual Indicators**: Color-coded performance

## 🌐 API Integration

### Authentication Flow
1. **Login**: Store JWT token in service
2. **API Calls**: Include token in Authorization header
3. **Logout**: Clear token and redirect to login
4. **Token Expiry**: Handle 401 responses gracefully

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
