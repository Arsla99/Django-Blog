# Quick Test Guide

This guide helps you quickly test all features of the Advanced Blog Platform.

## Prerequisites

Make sure the server is running:
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## Test Accounts

Use these pre-populated accounts:

| Role | Username | Password | Permissions |
|------|----------|----------|-------------|
| Admin | admin | admin123 | Full access |
| Author | john_author | author123 | Create/edit posts |
| Author | jane_author | author123 | Create/edit posts |
| Reader | reader1 | reader123 | View & comment |
| Reader | reader2 | reader123 | View & comment |

## Testing Checklist

### 1. Home Page (No Login Required)
- [ ] Visit http://127.0.0.1:8000/
- [ ] Verify posts are displayed in grid layout
- [ ] Check sidebar shows categories and tags
- [ ] Click on a post to view details
- [ ] Test search functionality
- [ ] Verify pagination works

### 2. Authentication Flow

#### Registration
- [ ] Click "Register" in navbar
- [ ] Fill out registration form
- [ ] Select role (Reader, Author)
- [ ] Submit and verify redirect to login

#### Login
- [ ] Click "Login" in navbar
- [ ] Enter credentials (try: admin / admin123)
- [ ] Verify successful login message
- [ ] Check navbar shows username and role badge
- [ ] Verify dropdown menu appears

#### Profile
- [ ] Click on username dropdown
- [ ] Select "Profile"
- [ ] Update profile information
- [ ] Upload profile image (optional)
- [ ] Save and verify changes

### 3. Reader Role Tests
Login as: `reader1` / `reader123`

- [ ] View published posts
- [ ] Click on a post
- [ ] Add a comment
- [ ] Verify "pending approval" message
- [ ] Try to access dashboard (should be denied)
- [ ] Try to create post (should be denied)

### 4. Author Role Tests
Login as: `john_author` / `author123`

#### Create Post
- [ ] Click "Create Post" in navbar
- [ ] Fill in title: "Test Post"
- [ ] Enter content using rich text editor
- [ ] Upload featured image (optional)
- [ ] Select category
- [ ] Select tags
- [ ] Set status to "Published"
- [ ] Submit and verify creation

#### Edit Post
- [ ] Go to Dashboard
- [ ] Click edit button on your post
- [ ] Modify content
- [ ] Save and verify changes

#### Delete Post
- [ ] Go to Dashboard
- [ ] Click delete button on your post
- [ ] Confirm deletion
- [ ] Verify post removed

#### Moderate Comments
- [ ] Go to Dashboard
- [ ] Check "Pending Comments" section
- [ ] Approve a comment
- [ ] Verify it appears on post
- [ ] Delete a comment

### 5. Admin Role Tests
Login as: `admin` / `admin123`

#### Dashboard
- [ ] Access dashboard
- [ ] View all posts (including other authors')
- [ ] View all pending comments
- [ ] Approve/delete any comment

#### Admin Panel
- [ ] Click "Admin Panel" in dropdown
- [ ] Navigate to Posts
- [ ] View customized admin interface
- [ ] Test filters (status, category, tags)
- [ ] Try bulk actions
- [ ] Edit a post inline
- [ ] View comments in post detail

#### Manage Categories
- [ ] Go to Admin → Categories
- [ ] Create new category
- [ ] Edit existing category
- [ ] Verify slug auto-generates

#### Manage Tags
- [ ] Go to Admin → Tags
- [ ] Create new tag
- [ ] Edit existing tag
- [ ] Verify slug auto-generates

### 6. Category & Tag Filtering
- [ ] Click on a category badge
- [ ] Verify filtered posts
- [ ] Check pagination
- [ ] Click on a tag
- [ ] Verify filtered posts

### 7. Search Functionality
- [ ] Use search bar in navbar
- [ ] Enter search term (e.g., "Django")
- [ ] Verify relevant results
- [ ] Try empty search
- [ ] Try search with no results

### 8. Post Features
- [ ] View post detail page
- [ ] Check view counter increments
- [ ] Verify featured image displays
- [ ] Check rich text formatting
- [ ] Verify tags are clickable
- [ ] Check author information
- [ ] Verify comment count

### 9. Comment System
- [ ] Post a comment as reader
- [ ] Verify "pending approval" status
- [ ] Login as author
- [ ] Approve the comment
- [ ] Verify comment now visible
- [ ] Post comment as author (should auto-approve)

### 10. UI/UX Tests
- [ ] Test on mobile viewport (responsive design)
- [ ] Verify all buttons have hover effects
- [ ] Check alerts dismiss properly
- [ ] Verify form validation works
- [ ] Check error messages display
- [ ] Test navigation flow

### 11. Security Tests
- [ ] Try accessing /blog/post/create/ as reader (should redirect)
- [ ] Try editing another author's post (should deny)
- [ ] Try deleting another author's post (should deny)
- [ ] Verify CSRF protection on forms
- [ ] Test logout functionality

### 12. Edge Cases
- [ ] Create post with very long title
- [ ] Upload large image file
- [ ] Submit empty comment
- [ ] Try duplicate slug
- [ ] Test special characters in search

## Expected Results

### ✅ All tests should pass with:
- Proper permission checks
- Clear error/success messages
- Responsive design on all devices
- Fast page loads
- No broken links or images
- Proper form validation
- Secure authentication

## Common Test Scenarios

### Scenario 1: New User Journey
1. Register as new user (reader)
2. Browse posts
3. Add comment
4. Update profile
5. Logout

### Scenario 2: Author Workflow
1. Login as author
2. Create draft post
3. Preview
4. Publish post
5. Moderate comments
6. View statistics

### Scenario 3: Admin Management
1. Login as admin
2. View all users
3. Manage posts from all authors
4. Moderate all comments
5. Create categories/tags
6. View analytics

## Performance Checks

- [ ] Home page loads < 2 seconds
- [ ] Post detail loads < 1 second
- [ ] Search returns results quickly
- [ ] Image uploads complete successfully
- [ ] Pagination is smooth

## Browser Compatibility

Test in multiple browsers:
- [ ] Chrome
- [ ] Firefox
- [ ] Edge
- [ ] Safari (if available)
- [ ] Mobile browsers

## Troubleshooting

### Issue: "No posts found"
**Solution**: Run `python manage.py populate_data`

### Issue: "Login required" on home page
**Solution**: Check `Post.status == 'published'`

### Issue: Images not displaying
**Solution**: 
1. Check MEDIA_URL in settings
2. Verify media files exist
3. Check URL configuration

### Issue: Search not working
**Solution**: Verify posts exist and are published

### Issue: Can't create post
**Solution**: 
1. Check user role (must be Author or Admin)
2. Verify all required fields filled
3. Check form validation errors

## Automated Testing (Optional)

Run Django tests:
```bash
python manage.py test
```

Create test cases for:
- Model creation
- View permissions
- Form validation
- URL routing

## Load Testing (Optional)

Use tools like:
- Apache Bench: `ab -n 100 -c 10 http://127.0.0.1:8000/`
- Locust: For stress testing
- Django Debug Toolbar: For query optimization

## Reporting Issues

If you find any issues:
1. Note the exact steps to reproduce
2. Check browser console for errors
3. Review Django logs
4. Verify database state
5. Check permissions

## Success Criteria

✅ **Project is working correctly if:**
- All user roles function properly
- Posts can be created, edited, deleted
- Comments require and get approval
- Search returns relevant results
- Images upload and display
- Responsive design works
- No security vulnerabilities
- Error handling is graceful
- Performance is acceptable

---

**Testing completed successfully?** 
You're ready to deploy! See `DEPLOYMENT.md` for next steps.
