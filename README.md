# sensAI

Your own sensei, using AI.

## What is sensAI?

sensAI is a **self-hostable AI-powered coding sensei** that helps students learn programming through guided code review and Socratic questioning. Instead of just fixing code, sensAI teaches students to think critically about their code and discover solutions themselves.

## 🚀 Key Features

### **🧘‍♂️ AI-Powered Teaching**
- **Code Review**: Paste your code and get educational feedback
- **Socratic Teaching**: Learn through guided questions rather than direct answers
- **Multiple Languages**: Support for Python, JavaScript, TypeScript, Java, C++, Go, Rust, and more
- **Real-time Streaming**: Get responses as the AI thinks

### **🏠 Self-Hostable**
- **One-click Docker deployment** - Deploy anywhere
- **GDPR Compliant** - Data export, deletion, and anonymization
- **Freemium Ready** - Rate limiting and usage tracking built-in
- **Session-based Authentication** - No complex user management needed
- **Conversation History** - Toggleable session storage

### **🔧 Modern Tech Stack**
- **Backend**: FastAPI + vLLM + Mistral-7B-Instruct-v0.3
- **Frontend**: Streamlit (modern, interactive UI)
- **Database**: SQLite (easily changeable to PostgreSQL)
- **AI Framework**: LangChain (prompt management)
- **ORM**: SQLAlchemy (database abstraction)

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- At least 8GB RAM (for the AI model)
- NVIDIA GPU recommended (for faster inference)

### One-Click Deployment

1. **Clone and start**:
   ```bash
   git clone https://github.com/Basmoussent/sensai.git
   cd sensai
   make
   ```

2. **Access the application**:
   - **Streamlit UI**: http://localhost:8501
   - **FastAPI Backend**: http://localhost:8000
   - **Health check**: http://localhost:8000/health

### Available Commands

```bash
# Docker Deployment
make              # One-click Docker deployment (default)
make restart      # Restart all services  
make stop         # Stop all services
make logs         # Show service logs
make clean        # Clean up everything

# Development
make setup-dev    # Setup development environment
make dev          # Run in development mode

# Database
make init-db      # Initialize database
make migrate      # Run migrations
make backup-db    # Backup database

# GDPR Compliance
make gdpr-export  # Export user data
make gdpr-delete  # Delete user data
make gdpr-anonymize # Anonymize user data

# Security & Testing
make security-check # Run security checks
make test         # Run tests
make test-coverage # Run tests with coverage
```

## 📖 How to Use

1. **Open the Streamlit interface** at http://localhost:8501
2. **Select your programming language** from the dropdown
3. **Paste your code** in the text area
4. **Optionally ask a specific question** about your code
5. **Click "Get Sensei Review"** and watch the AI analyze your code
6. **Learn through the AI's questions and explanations**

## 💡 Example

**Your Code:**
```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total / len(numbers)
```

**Sensei's Response:**
> Great start! I can see you're thinking about how to calculate an average. Let me ask you a few questions to help you think deeper:
> 
> 1. What happens if someone passes an empty list to your function?
> 2. What if they pass something that's not a list of numbers?
> 
> These are important considerations for writing robust code. How might you handle these cases?

## 🏗️ Architecture

### **Backend Services**
- **FastAPI**: REST API with streaming responses
- **vLLM**: High-performance inference engine
- **Mistral-7B-Instruct-v0.3**: AI model optimized for coding tasks
- **SQLAlchemy**: Database ORM with SQLite/PostgreSQL support
- **LangChain**: Prompt management and AI workflows

### **Frontend**
- **Streamlit**: Modern, interactive web interface
- **Real-time streaming**: Live AI responses
- **Dark theme**: Beautiful, modern UI
- **Responsive design**: Works on desktop and mobile

### **Deployment**
- **Docker Compose**: One-click deployment
- **Self-hostable**: Deploy anywhere
- **Production ready**: SSL support, monitoring, backups

## 🛠️ Development

### Development Setup

```bash
# Setup development environment with virtual environment
make setup-dev

# Run in development mode (Streamlit + FastAPI)
make dev

# Or manually:
source venv/bin/activate
pip install -e .
pip install -e ".[dev]"  # Install dev dependencies
```

### Project Structure

```
sensAI/
├── backend/                 # FastAPI backend
│   ├── main.py             # FastAPI application
│   ├── models/             # SQLAlchemy models
│   ├── services/           # Business logic
│   ├── scripts/            # Database and GDPR scripts
│   └── prompts.py          # LangChain prompt templates
├── frontend/               # Streamlit frontend
│   └── app.py             # Streamlit application
├── tests/                  # Test suite
├── docker-compose.yml      # Docker orchestration
├── pyproject.toml         # Python project configuration
└── Makefile               # Development commands
```

### Database Schema

- **Users**: User management (for future freemium features)
- **Sessions**: Session tracking and authentication
- **Conversations**: Code review history and AI responses
- **Usage Logs**: Rate limiting and analytics

## 🤖 AI Model Information

sensAI uses **Mistral-7B-Instruct-v0.3**, a powerful language model fine-tuned for instruction following. The model is optimized for:

- **Code understanding and analysis**
- **Educational explanations**
- **Socratic questioning techniques**
- **Multiple programming languages**

### Model Configuration
- **Size**: ~13GB (7 billion parameters)
- **Memory**: Requires 8GB+ RAM
- **GPU**: NVIDIA GPU recommended for faster inference
- **Quantization**: Supports FP16 for efficiency

## 🔒 GDPR Compliance

sensAI is built with privacy and compliance in mind:

### **Data Rights**
- **Right to Access**: Export all your data (`make gdpr-export`)
- **Right to Erasure**: Delete all your data (`make gdpr-delete`)
- **Right to Anonymization**: Anonymize personal data (`make gdpr-anonymize`)

### **Data Handling**
- **Minimal data collection**: Only what's necessary for functionality
- **Session-based**: No persistent user accounts by default
- **Local storage**: Data stays on your infrastructure
- **Encryption**: Data encrypted in transit and at rest

## 🚀 Deployment Options

### **Self-Hosted (Recommended)**
```bash
# One-click deployment
make

# Production deployment with SSL
make deploy-prod
```

### **Cloud Deployment**
- **Railway**: `railway up`
- **Render**: Connect GitHub repository
- **DigitalOcean**: Docker droplet deployment
- **AWS/GCP/Azure**: Container service deployment

## 🛠️ Troubleshooting

### Common Issues

1. **Out of Memory**: Ensure you have at least 8GB RAM available
2. **Slow Responses**: Consider using a GPU for faster inference
3. **Model Download**: First run may take time to download the model (~13GB)
4. **Port Conflicts**: Change ports in docker-compose.yml if needed

### Health Checks

- **Backend**: http://localhost:8000/health
- **Frontend**: http://localhost:8501
- **Logs**: `make logs`

### Security

- **Rate Limiting**: Built-in protection against abuse
- **Input Sanitization**: Code injection protection
- **CORS**: Proper cross-origin policies
- **Security Check**: `make security-check`

## 🎯 Roadmap

### **Phase 1: Self-Hostable MVP** ✅
- [x] Docker deployment
- [x] GDPR compliance
- [x] Session-based authentication
- [x] Code review functionality

### **Phase 2: Enhanced Features** 🚧
- [ ] User accounts and authentication
- [ ] Conversation history persistence
- [ ] Advanced code analysis features
- [ ] Multiple AI model support

### **Phase 3: Public SaaS** 📋
- [ ] Freemium model implementation
- [ ] Multi-tenant architecture
- [ ] Advanced analytics dashboard
- [ ] API for third-party integrations

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
git clone https://github.com/Basmoussent/sensai.git
cd sensai
make setup-dev
make dev
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Mistral AI** for the excellent language model
- **vLLM** team for the high-performance inference engine
- **Streamlit** for the beautiful UI framework
- **FastAPI** for the modern Python web framework

---

**Built with ❤️ for students learning to code**

**🧘‍♂️ Your AI coding sensei awaits!**