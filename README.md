# AI Powered Blog Post Generator

An intelligent blog post generation system that uses AI to create SEO-optimized content. This application automatically generates blog posts based on keywords, incorporates SEO best practices, and provides a clean web interface for content management.

## Features

- 🤖 AI-powered blog post generation using NVIDIA's AI models
- 📊 SEO optimization with real-time metrics
- 📝 Markdown to HTML conversion
- 🔄 Automated daily post generation
- 📱 Responsive web interface
- 🔍 Source management and verification
- 📈 SEO performance tracking
- 🗑️ Content management system

## Prerequisites

- Python 3.8 or higher
- NVIDIA API key
- Flask
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-blog-generator.git
cd ai-blog-generator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv blogEnv
.\blogEnv\Scripts\activate

# Linux/Mac
python3 -m venv blogEnv
source blogEnv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API keys:
```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

## Project Structure

```
ai-blog-generator/
├── app.py                 # Main Flask application
├── ai_generator.py        # AI content generation logic
├── seo_fetcher.py         # SEO data fetching
├── seo_template.html      # SEO metrics template
├── requirements.txt       # Project dependencies
├── data/                  # Data storage
│   └── blogsDb.json      # Blog posts database
├── generated_posts/       # Generated content storage
├── templates/            # HTML templates
│   ├── index.html        # Main page template
│   └── blog_post.html    # Blog post template
└── blogEnv/              # Virtual environment
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Access the web interface:
- Open your browser and navigate to `http://localhost:5000`
- The main page will display all generated blog posts
- Click on any post to view its full content

3. Generate a new blog post:
- Use the `/generate` endpoint with a keyword parameter
- Example: `http://localhost:5000/generate?keyword=wireless-earbuds`

4. View a specific post:
- Access posts using the `/post/<filename>` endpoint
- Example: `http://localhost:5000/post/wireless-earbuds`

## API Endpoints

### Main Endpoints

- `GET /`: Home page with list of all blog posts
- `GET /post/<filename>`: View a specific blog post
- `GET /generate`: Generate a new blog post
- `POST /delete_post/<keyword>`: Delete a blog post
- `GET /health`: Health check endpoint

### Helper Functions

- `load_blog_posts()`: Load posts from JSON database
- `save_blog_posts()`: Save posts to JSON database
- `sanitize_word()`: Sanitize keywords for filenames
- `extract_title_from_markdown()`: Extract titles from content
- `save_post_json()`: Save generated posts as JSON
- `generate_daily_post()`: Scheduled post generation

## Content Generation

The system generates blog posts with the following structure:

1. Title
2. Introduction (2 paragraphs)
3. Main Content
   - Simple explanations
   - Practical examples
   - Detailed explanations
   - Step-by-step breakdowns
   - Common misconceptions
   - Benefits and challenges
   - Current trends
4. Future Outlook
5. Conclusion
6. Sources (3-5 reputable sources)

## SEO Integration

Each generated post includes:
- Search volume
- Keyword difficulty
- Average CPC (Cost Per Click)
- SEO-optimized content structure

## Automated Features

- Daily post generation using random keywords
- SEO data fetching and integration
- Markdown to HTML conversion
- Source verification and management

## Error Handling

The application includes comprehensive error handling for:
- Database operations
- Post generation
- Template formatting
- File operations
- API requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NVIDIA AI Models
- Flask Framework
- Python Community

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Future Enhancements

- [ ] Social media integration
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] Custom AI model integration
- [ ] Advanced SEO optimization
- [ ] Content scheduling system
- [ ] User authentication system 