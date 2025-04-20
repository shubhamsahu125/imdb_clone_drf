IMDB API Clone With DRF
🔗 Final Project Links (Arranged According To Usage)

1. Admin Access
- Admin Section: http://127.0.0.1:8000/dashboard/

2. Accounts
- Registration: http://127.0.0.1:8000/api/account/register/
- Login: http://127.0.0.1:8000/api/account/login/
- Logout: http://127.0.0.1:8000/api/account/logout/

3. Stream Platforms
- Create Element & Access List: http://127.0.0.1:8000/api/watch/stream/
- Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/

4. Watch List
- Create & Access List: http://127.0.0.1:8000/api/watch/
- Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/<int:movie_id>/

5. Reviews
- Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/
- List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/
- Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/

6. User Review
- Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example
