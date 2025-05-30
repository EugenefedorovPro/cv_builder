/media/photos/Eugene_Proskulikov_photo_2020-07-07_.jpg

______________________
settings.py: 

    STATIC_URL = "static/"
    STATIC_ROOT = BASE_DIR / "staticfiles"

    MEDIA_URL = "media/"
    MEDIA_ROOT = BASE_DIR / "media"

models.py

    class Photos(models.Model):
        photo_url = models.ImageField(blank = True, null = True, upload_to = "photos/")

urls.py in project:

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

I do not see any photos in my media folder?

____________________
I work with React TS.

I see two ways of splitting my code to separate parts:
First approach with three files:
- fetch data from back with axios
- import data to component which react bootstrap
- import component to general Layout.

Second approach with two files
- fetch data from back with axios and populate bootstrap fields in the same file
- import component to general Layout.

which approach is better?
what are alternatives?


________________________________________
def save(self, *args):
    self.user = request.user
    super().save(*args)


I want the user of my django app to have access only to instances of the model he has created.
The point this is that I use standard admin contrib from django. 
What are the best practices of doing this?



________________________________________
How to make Navbar vertical for large screens and horizontal for md and sm?
I have already created the grid and going to insert NavbarCV to Col, which bevhaves as I want.
Actually, I need NavbarCV to adapt to the behaviour of that column.
I want only fragment of this code with expalnation in react bootstrap.
Do not provide all Navbar.

Navbar:

    return (
        <Navbar expand="lg" className="bg-body-tertiary">
            <Navbar.Brand href="/">CV</Navbar.Brand>
            <Nav className="me-auto">
                <Nav.Link href="#cases">Cases</Nav.Link>
                <Nav.Link href="#why-me">Cases</Nav.Link>
                <Nav.Link href="#feedback">Cases</Nav.Link>
            </Nav>
            <Nav className="ms-auto">
                <Nav.Link>eng</Nav.Link>
            </Nav>
        </Navbar>

    )
Navbar is placed into this context.

    return (<>
        <Container
            fluid
            className="p-0"

        >
            <Row
                className="g-0"
            >

                <Col
                    xl={2}
                    xs={12}
                    xm={12}
                    className="navbar-col d-flex flex-column bg-info"
                >
                    {<NavbarCV/>}
                </Col>

...
________________
Context: React Type Script, react-bootstrap, bootstrap, css only when needed.
________________

