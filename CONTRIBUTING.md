# Contributing to Advanced Blog Platform

Thank you for your interest in contributing to the Advanced Blog Platform! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version, Django version)

### Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature already exists
- Provide clear use cases
- Explain why it would be valuable
- Consider implementation complexity

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: Feature description"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## 📝 Coding Standards

### Python Code Style
- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Maximum line length: 120 characters

Example:
```python
def calculate_reading_time(content):
    """
    Calculate estimated reading time for a post.
    
    Args:
        content (str): The post content
        
    Returns:
        int: Estimated reading time in minutes
    """
    word_count = len(content.split())
    return max(1, word_count // 200)
```

### Django Best Practices
- Use class-based views where appropriate
- Implement proper permission checks
- Use Django ORM efficiently (select_related, prefetch_related)
- Follow Django's security best practices
- Write reusable code

### HTML/CSS Standards
- Use semantic HTML5 elements
- Follow Bootstrap conventions
- Keep CSS organized and commented
- Ensure responsive design
- Test across browsers

### JavaScript Standards
- Use modern ES6+ syntax
- Add comments for complex logic
- Follow consistent naming conventions
- Minimize inline JavaScript

## 🧪 Testing

### Before Submitting
- [ ] Run all existing tests: `python manage.py test`
- [ ] Test manually in browser
- [ ] Check responsive design
- [ ] Verify no console errors
- [ ] Test with different user roles

### Writing Tests
- Write unit tests for models
- Write integration tests for views
- Test edge cases
- Aim for good coverage

Example test:
```python
from django.test import TestCase
from blog.models import Post
from accounts.models import CustomUser

class PostModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass123',
            role='author'
        )
        
    def test_post_creation(self):
        post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
            status='published'
        )
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(str(post), 'Test Post')
```

## 📦 Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add: New feature or functionality
Fix: Bug fix
Update: Modify existing feature
Remove: Delete code or files
Docs: Documentation changes
Style: Code style/formatting
Refactor: Code restructuring
Test: Add or update tests
```

Examples:
```bash
git commit -m "Add: Email notification for new comments"
git commit -m "Fix: Pagination issue on search results"
git commit -m "Update: Improve dashboard UI layout"
```

## 🌿 Branch Naming

Use descriptive branch names:
- `feature/feature-name` - New features
- `fix/bug-description` - Bug fixes
- `docs/documentation-update` - Documentation
- `refactor/code-improvement` - Code refactoring

## 📋 Pull Request Process

1. **Update Documentation**
   - Update README if needed
   - Add docstrings
   - Update CHANGELOG

2. **Code Review**
   - Address review comments
   - Keep PR focused
   - Don't mix unrelated changes

3. **Merge Requirements**
   - All tests pass
   - Code follows style guide
   - Documentation updated
   - No merge conflicts

## 🔍 Code Review Guidelines

### As a Reviewer
- Be respectful and constructive
- Focus on code, not the person
- Explain reasoning behind suggestions
- Approve when ready

### As a Contributor
- Don't take feedback personally
- Ask questions if unclear
- Discuss technical disagreements
- Be patient

## 🚀 Development Setup

1. Fork and clone the repository
2. Create virtual environment
3. Install dependencies
4. Run migrations
5. Populate sample data
6. Start development server

```bash
git clone your-fork-url
cd advanced-blog
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py populate_data
python manage.py runserver
```

## 📚 Resources

### Django Documentation
- [Django Docs](https://docs.djangoproject.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/misc/design-philosophies/)
- [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)

### Python Resources
- [PEP 8](https://pep8.org/)
- [Python Documentation](https://docs.python.org/)

### Frontend Resources
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [MDN Web Docs](https://developer.mozilla.org/)

## 🎯 Priority Areas

Areas where contributions are especially welcome:

### High Priority
- [ ] Unit test coverage
- [ ] Performance optimization
- [ ] Accessibility improvements
- [ ] Security enhancements

### Medium Priority
- [ ] Additional features (see README roadmap)
- [ ] UI/UX improvements
- [ ] Documentation enhancements
- [ ] Code refactoring

### Low Priority
- [ ] Minor bug fixes
- [ ] Code style improvements
- [ ] Comment additions

## 🐛 Found a Security Issue?

**Do NOT create a public issue!**

Instead:
1. Email details to: security@yourblog.com
2. Include description and steps to reproduce
3. Wait for acknowledgment
4. Allow time for fix before disclosure

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## 💬 Questions?

- Open a discussion issue
- Ask in pull request comments
- Check existing documentation

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!

---

**Happy Coding!** 🚀
