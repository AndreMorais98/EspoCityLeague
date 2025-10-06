# ⚛️ Espo City League Frontend

<div align="center">

**React + TypeScript Frontend for Espo City League Football Prediction Platform**

[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![SCSS](https://img.shields.io/badge/SCSS-CC6699?style=for-the-badge&logo=sass&logoColor=white)](https://sass-lang.com/)
[![Create React App](https://img.shields.io/badge/Create%20React%20App-09D3AC?style=for-the-badge&logo=create-react-app&logoColor=white)](https://create-react-app.dev/)

</div>

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🎨 UI Components](#-ui-components)
- [🔧 State Management](#-state-management)
- [🌐 API Integration](#-api-integration)
- [🎨 Styling](#-styling)
- [🧪 Testing](#-testing)
- [📦 Build & Deployment](#-build--deployment)
- [🛠️ Development](#️-development)

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
BACKEND_URL=BACKEND_URL
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

### Contexts (`src/contexts/`)

#### UserContext
```typescript
interface UserContextType {
  user: User | null;
  setUser: (user: User | null) => void;
  login: (username: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}
```

#### SidebarContext
```typescript
interface SidebarContextType {
  isCollapsed: boolean;
  setIsCollapsed: (collapsed: boolean) => void;
  toggleSidebar: () => void;
}
```

## 🎨 UI Components

### Component Structure
```typescript
// Example component structure
import React, { useState, useEffect } from 'react';
import { useUser } from '../../contexts/UserContext';
import { apiService } from '../../services/api';
import './ComponentName.scss';

interface ComponentNameProps {
  title: string;
  onAction?: () => void;
}

export default function ComponentName({ title, onAction }: ComponentNameProps) {
  const { user } = useUser();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Component logic here
  }, []);

  return (
    <div className="component-name">
      <h2>{title}</h2>
      {/* Component content */}
    </div>
  );
}
```

### Styling Convention
```scss
// ComponentName.scss
.component-name {
  padding: 16px;
  background: var(--background-color);
  
  &__title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 16px;
  }
  
  &__button {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background: var(--primary-color);
    color: white;
    cursor: pointer;
    
    &:hover {
      background: var(--primary-hover-color);
    }
  }
}
```

## 🔧 State Management

### Context Providers
- **UserContext**: Global user authentication state
- **SidebarContext**: Sidebar collapse/expand state
- **ThemeContext**: Future theme management

### State Patterns
```typescript
// Local state for component-specific data
const [loading, setLoading] = useState(false);
const [data, setData] = useState<DataType[]>([]);

// Context state for global data
const { user, setUser } = useUser();
const { isCollapsed, toggleSidebar } = useSidebar();
```

### Data Flow
1. **API Calls**: Centralized in `services/api.ts`
2. **State Updates**: Through context providers
3. **Component Re-renders**: Automatic with React hooks
4. **Error Handling**: Try-catch blocks with user feedback

## 🌐 API Integration

### API Service Layer
```typescript
// services/api.ts
class ApiService {
  private baseURL: string;
  private token: string | null = null;

  async login(username: string, password: string): Promise<LoginResponse> {
    const response = await this.makeRequest<LoginResponse>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    });
    
    this.token = response.access_token;
    return response;
  }

  async getStages(): Promise<Stage[]> {
    return this.makeRequest<Stage[]>('/stages/');
  }
}
```

### Error Handling
```typescript
// Centralized error handling
try {
  const data = await apiService.getStages();
  setStages(data);
} catch (error: any) {
  console.error('Error loading stages:', error);
  setError(error.message || 'Failed to load stages');
}
```

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

## 🧪 Testing

### Running Tests
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run specific test file
npm test ComponentName.test.tsx
```

### Test Structure
```typescript
// ComponentName.test.tsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { UserProvider } from '../../contexts/UserContext';
import ComponentName from './ComponentName';

const renderWithProviders = (component: React.ReactElement) => {
  return render(
    <BrowserRouter>
      <UserProvider>
        {component}
      </UserProvider>
    </BrowserRouter>
  );
};

describe('ComponentName', () => {
  it('renders title correctly', () => {
    renderWithProviders(<ComponentName title="Test Title" />);
    expect(screen.getByText('Test Title')).toBeInTheDocument();
  });

  it('handles user interaction', () => {
    const mockAction = jest.fn();
    renderWithProviders(<ComponentName title="Test" onAction={mockAction} />);
    
    fireEvent.click(screen.getByRole('button'));
    expect(mockAction).toHaveBeenCalledTimes(1);
  });
});
```

### Testing Tools
- **React Testing Library**: Component testing utilities
- **Jest**: Test runner and assertion library
- **MSW**: API mocking for integration tests
- **Testing Utilities**: Custom render functions with providers

## 📦 Build & Deployment

### Build Process
```bash
# Development server
npm start

# Production build
npm run build

# Test the application
npm test
```

### Deployment Options
- **Vercel**: Zero-config deployment with automatic builds
- **Netlify**: Static site hosting with form handling
- **GitHub Pages**: Free hosting for public repositories
- **Docker**: Containerized deployment

### Environment Variables
```bash
# .env.local
REACT_APP_API_URL=http://localhost:8000
REACT_APP_APP_NAME=Espo City League
REACT_APP_VERSION=1.0.0
```

## 🛠️ Development

### Development Tools
```bash
# Code formatting
npm run format

# Linting
npm run lint

# Type checking
npm run type-check

# Fix linting issues
npm run lint:fix
```

### Code Quality
- **ESLint**: Code linting with React and TypeScript rules
- **Prettier**: Code formatting for consistency
- **TypeScript**: Static type checking
- **Husky**: Git hooks for pre-commit checks

### Development Scripts
```json
{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "lint:fix": "eslint . --ext ts,tsx --fix",
    "format": "prettier --write \"src/**/*.{ts,tsx,scss}\"",
    "type-check": "tsc --noEmit"
  }
}
```

### Hot Reload
- **Fast Refresh**: Instant component updates during development
- **CSS Hot Reload**: Immediate style changes
- **TypeScript**: Real-time type checking
- **Error Overlay**: Clear error messages in browser

## 🔧 Configuration

### TypeScript Configuration
```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "es6"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src"
  ]
}
```

### ESLint Configuration
```json
// .eslintrc.json
{
  "extends": [
    "react-app",
    "react-app/jest"
  ],
  "rules": {
    "react-hooks/exhaustive-deps": "warn",
    "@typescript-eslint/no-unused-vars": "error"
  }
}
```

## 📚 Additional Resources

- [React Documentation](https://reactjs.org/docs/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Create React App Documentation](https://create-react-app.dev/)
- [React Router Documentation](https://reactrouter.com/)
- [SCSS Documentation](https://sass-lang.com/documentation)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

For detailed contribution guidelines, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

<div align="center">

**Built with ❤️ using React + TypeScript**

[Report Bug](https://github.com/yourusername/espo-city-league/issues) · [Request Feature](https://github.com/yourusername/espo-city-league/issues)

</div>