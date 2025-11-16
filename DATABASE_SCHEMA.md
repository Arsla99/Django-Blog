# Database Schema Diagram

## Entity Relationship Diagram

```
┌─────────────────────────────────────┐
│         CustomUser (accounts)       │
├─────────────────────────────────────┤
│ PK │ id (AutoField)                 │
│    │ username (CharField, unique)   │
│    │ email (EmailField)             │
│    │ password (CharField)           │
│    │ first_name (CharField)         │
│    │ last_name (CharField)          │
│    │ role (CharField)               │
│    │   - admin                      │
│    │   - author                     │
│    │   - reader (default)           │
│    │ bio (TextField, nullable)      │
│    │ profile_image (ImageField)     │
│    │ is_staff (BooleanField)        │
│    │ is_active (BooleanField)       │
│    │ is_superuser (BooleanField)    │
│    │ date_joined (DateTimeField)    │
│    │ last_activity (DateTimeField)  │
└─────────────────────────────────────┘
            │
            │ 1:N (author)
            │
            ▼
┌─────────────────────────────────────┐
│           Post (blog)               │
├─────────────────────────────────────┤
│ PK │ id (AutoField)                 │
│    │ title (CharField, max=200)     │
│    │ slug (SlugField, unique)       │
│    │ content (RichTextField)        │
│    │ excerpt (TextField)            │
│    │ featured_image (ImageField)    │
│ FK │ author → CustomUser.id         │
│ FK │ category → Category.id         │
│    │ status (CharField)             │
│    │   - draft                      │
│    │   - published                  │
│    │ views (PositiveIntegerField)   │
│    │ created_at (DateTimeField)     │
│    │ updated_at (DateTimeField)     │
│    │ published_at (DateTimeField)   │
└─────────────────────────────────────┘
            │                    │
            │ N:1                │ 1:N
            ▼                    ▼
┌──────────────────────┐  ┌──────────────────────┐
│   Category (blog)    │  │    Comment (blog)    │
├──────────────────────┤  ├──────────────────────┤
│ PK │ id (AutoField)  │  │ PK │ id (AutoField)  │
│    │ name (CharField)│  │ FK │ post → Post.id  │
│    │ slug (SlugField)│  │ FK │ user → User.id  │
│    │ description     │  │    │ content         │
│    │ created_at      │  │    │ approved        │
└──────────────────────┘  │    │ created_at      │
                          │    │ updated_at      │
                          └──────────────────────┘
            ▲                    ▲
            │ N:1                │ 1:N
            │                    │
┌──────────────────────┐         │
│      Tag (blog)      │         │
├──────────────────────┤         │
│ PK │ id (AutoField)  │         │
│    │ name (CharField)│         │
│    │ slug (SlugField)│         │
│    │ created_at      │         │
└──────────────────────┘         │
            ▲                    │
            │                    │
            │ M:N                │
            │                    │
┌──────────────────────┐         │
│   Post_tags          │         │
│   (Many-to-Many)     │         │
├──────────────────────┤         │
│ PK │ id              │         │
│ FK │ post_id         │         │
│ FK │ tag_id          │         │
└──────────────────────┘         │
                                 │
┌─────────────────────────────────┘
│         CustomUser
│       (1:N relationship)
└─────────────────────────────────┐
```

## Relationships

### One-to-Many Relationships

1. **CustomUser → Post** (author)
   - One user can create many posts
   - Each post has one author
   - Foreign Key: `Post.author`

2. **Category → Post**
   - One category can have many posts
   - Each post belongs to one category
   - Foreign Key: `Post.category`
   - On Delete: SET_NULL

3. **Post → Comment**
   - One post can have many comments
   - Each comment belongs to one post
   - Foreign Key: `Comment.post`
   - On Delete: CASCADE

4. **CustomUser → Comment**
   - One user can write many comments
   - Each comment has one author
   - Foreign Key: `Comment.user`
   - On Delete: CASCADE

### Many-to-Many Relationships

1. **Post ↔ Tag**
   - One post can have many tags
   - One tag can be applied to many posts
   - Through: Django-managed intermediary table `blog_post_tags`

## Field Details

### CustomUser Model
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PK | Primary key |
| username | CharField(150) | Unique, Required | Username for login |
| email | EmailField | Required | User email address |
| password | CharField(128) | Required | Hashed password |
| first_name | CharField(150) | Optional | User's first name |
| last_name | CharField(150) | Optional | User's last name |
| role | CharField(10) | Choices, Default='reader' | User role (admin/author/reader) |
| bio | TextField | Nullable | User biography |
| profile_image | ImageField | Nullable | Profile picture |
| is_staff | BooleanField | Default=False | Admin access |
| is_active | BooleanField | Default=True | Account status |
| is_superuser | BooleanField | Default=False | Superuser status |
| date_joined | DateTimeField | Auto | Registration date |
| last_activity | DateTimeField | Auto | Last activity timestamp |

### Post Model
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PK | Primary key |
| title | CharField(200) | Required | Post title |
| slug | SlugField(200) | Unique, Required | SEO-friendly URL |
| content | RichTextField | Required | Post content (HTML) |
| excerpt | TextField(500) | Optional | Brief description |
| featured_image | ImageField | Nullable | Post thumbnail |
| author | ForeignKey | Required, FK to User | Post author |
| category | ForeignKey | Nullable, FK to Category | Post category |
| status | CharField(10) | Choices, Default='draft' | Publication status |
| views | PositiveIntegerField | Default=0 | View count |
| created_at | DateTimeField | Auto | Creation timestamp |
| updated_at | DateTimeField | Auto | Last update timestamp |
| published_at | DateTimeField | Nullable | Publication timestamp |

### Category Model
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PK | Primary key |
| name | CharField(100) | Unique, Required | Category name |
| slug | SlugField(100) | Unique, Required | SEO-friendly URL |
| description | TextField | Optional | Category description |
| created_at | DateTimeField | Auto | Creation timestamp |

### Tag Model
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PK | Primary key |
| name | CharField(50) | Unique, Required | Tag name |
| slug | SlugField(50) | Unique, Required | SEO-friendly URL |
| created_at | DateTimeField | Auto | Creation timestamp |

### Comment Model
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | AutoField | PK | Primary key |
| post | ForeignKey | Required, FK to Post | Associated post |
| user | ForeignKey | Required, FK to User | Comment author |
| content | TextField | Required | Comment text |
| approved | BooleanField | Default=False | Approval status |
| created_at | DateTimeField | Auto | Creation timestamp |
| updated_at | DateTimeField | Auto | Last update timestamp |

## Indexes

### Post Model
- Index on `created_at` (descending) for listing pages
- Index on `status` for filtering published posts

### Comment Model
- Composite index on `(post, created_at)` for efficient comment retrieval

## Database Constraints

1. **Unique Constraints**
   - CustomUser.username
   - Post.slug
   - Category.slug
   - Tag.slug

2. **Foreign Key Constraints**
   - Post.author → CustomUser (ON DELETE: CASCADE)
   - Post.category → Category (ON DELETE: SET NULL)
   - Comment.post → Post (ON DELETE: CASCADE)
   - Comment.user → CustomUser (ON DELETE: CASCADE)

3. **Check Constraints**
   - Post.status ∈ {'draft', 'published'}
   - CustomUser.role ∈ {'admin', 'author', 'reader'}

## Data Flows

### Post Creation Flow
```
User (Author) → Post (Draft) → Post (Published) → Visible to Readers
```

### Comment Flow
```
User (Any) → Comment (Unapproved) → Author/Admin Review → Comment (Approved) → Visible to All
```

### User Activity Tracking
```
User Request → Middleware → Update last_activity → Database
```

### Post Publication Signal
```
Post.save() → pre_save signal → Set published_at → post_save signal → Notification
```

## Performance Optimizations

1. **Select Related**: Used in views to reduce database queries
   - Post queries include `select_related('author', 'category')`
   - Comment queries include `select_related('user', 'post')`

2. **Prefetch Related**: Used for many-to-many relationships
   - Post queries include `prefetch_related('tags')`

3. **Indexes**: Strategic indexes on frequently queried fields
   - Post: created_at, status
   - Comment: post + created_at

4. **Pagination**: All list views implement pagination to limit query results

## Migration History

1. Initial migration: Creates all models and relationships
2. Indexes added for performance optimization
3. Custom user model extends AbstractUser
