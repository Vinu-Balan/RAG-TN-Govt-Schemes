# RAG Government Assistant Frontend

A modern React/Next.js frontend for the Government Schemes RAG Assistant with real-time streaming chat interface.

## Features

- **Real-time Streaming**: Live streaming responses from the RAG backend
- **Markdown Support**: Rich text rendering with GitHub Flavored Markdown
- **Responsive Design**: Mobile-first design with Tailwind CSS
- **Interactive UI**: Smooth animations and user-friendly interface
- **Source Citations**: Display of source links for retrieved information
- **Quick Suggestions**: Pre-defined query suggestions for common topics

## Tech Stack

- **Next.js 16**: React framework with App Router
- **React 19**: Latest React with concurrent features
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first CSS framework
- **React Markdown**: Markdown rendering with GFM support
- **Framer Motion**: Smooth animations and transitions

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd frontend/rag-govt
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

The application will be available at `http://localhost:3000`

## Usage

### Development

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linting
npm run lint
```

### Configuration

The frontend connects to the backend API at `http://127.0.0.1:8000` by default. To change this:

1. Update the API URL in `app/page.tsx`:
   ```typescript
   const res = await fetch("YOUR_API_URL/chat", {
     // ...
   });
   ```

2. For production deployment, set the API URL via environment variables.

## Project Structure

```
app/
├── globals.css          # Global styles and Tailwind imports
├── layout.tsx           # Root layout component
├── page.tsx             # Main chat interface
└── ...

public/                  # Static assets
├── favicon.ico
└── ...

package.json             # Dependencies and scripts
tailwind.config.js       # Tailwind configuration
next.config.ts          # Next.js configuration
```

## Key Components

### Chat Interface (`page.tsx`)

- **Message Display**: Shows user and assistant messages with proper styling
- **Streaming Animation**: Animated cursor during response generation
- **Source Links**: Clickable source citations below responses
- **Input Handling**: Real-time input with Enter key support
- **Loading States**: Visual feedback during API calls

### Features

- **Streaming Response Handling**: Processes server-sent events for real-time updates
- **Markdown Rendering**: Converts plain text responses to formatted markdown
- **Auto-scroll**: Automatically scrolls to latest messages
- **Error Handling**: Graceful error handling with console logging
- **Responsive Layout**: Adapts to different screen sizes

## API Integration

The frontend communicates with the FastAPI backend through:

- **Endpoint**: `POST /chat`
- **Request Format**: `{"query": "user question"}`
- **Response Format**: Streaming NDJSON with token and end events

### Streaming Protocol

```json
// Token events (multiple)
{"type": "token", "content": "response text chunk"}

// End event (final)
{"type": "end", "sources": ["source_url_1", "source_url_2"]}
```

## Styling

### Design System

- **Colors**: Blue primary (#3B82F6) with gray neutrals
- **Typography**: System fonts with proper hierarchy
- **Spacing**: Consistent 4px grid system
- **Components**: Rounded corners, subtle shadows, hover effects

### Tailwind Configuration

Custom Tailwind setup with:
- Typography plugin for markdown styling
- Custom color palette
- Responsive breakpoints
- Dark mode support (extendable)

## Development Guidelines

### Code Style

- **TypeScript**: Strict type checking enabled
- **ESLint**: Next.js recommended rules
- **Prettier**: Code formatting (if configured)

### Component Patterns

- **Functional Components**: Modern React patterns
- **Hooks**: useState, useEffect, useRef for state management
- **Event Handlers**: Proper TypeScript typing for events
- **Conditional Rendering**: Clean JSX with logical operators

### Performance

- **Code Splitting**: Automatic with Next.js App Router
- **Image Optimization**: Built-in Next.js Image component (extendable)
- **Bundle Analysis**: Check bundle size with build output

## Deployment

### Vercel (Recommended)

1. **Connect Repository**: Link your GitHub repo to Vercel
2. **Configure Build**: Next.js detects settings automatically
3. **Environment Variables**: Set API_URL for production backend
4. **Deploy**: Automatic deployments on push

### Manual Deployment

```bash
# Build the application
npm run build

# Start production server
npm start
```

### Docker Deployment

```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
```

## Browser Support

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile**: iOS Safari, Chrome Mobile
- **Fallbacks**: Graceful degradation for older browsers

## Contributing

1. **Fork and Clone**: Create your own fork
2. **Branch**: Create feature branches from main
3. **Develop**: Follow the established patterns
4. **Test**: Test across different browsers and devices
5. **Pull Request**: Submit with clear description

### Adding New Features

1. **Plan**: Discuss feature requirements
2. **Implement**: Follow TypeScript and React best practices
3. **Style**: Maintain design consistency
4. **Test**: Manual testing across devices
5. **Document**: Update this README if needed

## Troubleshooting

### Common Issues

1. **API Connection Failed**
   - Ensure backend is running on port 8000
   - Check CORS configuration
   - Verify API endpoint URL

2. **Streaming Not Working**
   - Check browser console for errors
   - Verify backend streaming implementation
   - Test with simple curl request

3. **Styling Issues**
   - Clear Next.js cache: `rm -rf .next`
   - Restart development server
   - Check Tailwind configuration

### Development Tips

- **Hot Reload**: Changes reflect immediately in development
- **Type Checking**: Run `npx tsc --noEmit` for type errors
- **Linting**: Run `npm run lint` before committing
- **Console Logging**: Use browser dev tools for debugging

## License

This project is licensed under the MIT License.
