IMDB API Clone With DRF <br>
---
🔗 Final Project Links (Arranged According To Usage)

1. Admin Access
&nbsp;- Admin Section: http://127.0.0.1:8000/dashboard/

2. Accounts
&nbsp;- Registration: http://127.0.0.1:8000/api/account/register/
&nbsp;- Login: http://127.0.0.1:8000/api/account/login/
&nbsp;- Logout: http://127.0.0.1:8000/api/account/logout/

3. Stream Platforms
&nbsp;- Create Element & Access List: http://127.0.0.1:8000/api/watch/stream/
&nbsp;- Access, Update & Destroy Individual Element: [http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/](http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/)

4. Watch List
&nbsp;- Create & Access List: http://127.0.0.1:8000/api/watch/
&nbsp;- Access, Update & Destroy Individual Element: [http://127.0.0.1:8000/api/watch/<int:movie_id>/](http://127.0.0.1:8000/api/watch/<int:movie_id>/)

5. Reviews
&nbsp;- Create Review For Specific Movie: [http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/](http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/)
&nbsp;- List Of All Reviews For Specific Movie: [http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/](http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/)
&nbsp;- Access, Update & Destroy Individual Review: [http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/](http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/)

6. User Review
&nbsp;- Access All Reviews For Specific User: [http://127.0.0.1:8000/api/watch/user-reviews/?username=example](http://127.0.0.1:8000/api/watch/user-reviews/?username=example)
