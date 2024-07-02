import asyncio
from zenaura.client.app import Route, App, HistoryNode
from zenaura.client.page import Page
from public.routes import ClientRoutes
from public.components.header import Header
from public.components.intro import IntroSection
from public.components.footer import Footer
from public.components.components import Components
from public.components.examples import Example
from zenaura.client.layout import Layout

try :
    from pyscript import window, document
except ImportError:
    from zenaura.client.mocks import MockWindow
    window = MockWindow()

event_loop = asyncio.get_event_loop()

import asyncio

router = App()

# Instantiate components
nav_bar_header = Header(router)
intro_section = IntroSection()
footer = Footer()
components = Components()
example = Example() 

# hoc 

# App and routing
home_page = Page([intro_section])
components_page = Page([components])
example_page = Page([example])

router.add_route(Route(
    title="Developer-Focused | Zenaura",
    path=ClientRoutes.home.value,
    page=home_page
))


router.add_route(Route(
    title="components",
    path=ClientRoutes.components.value,
    page=components_page
))


router.add_route(Route(
    title="example",
    path=ClientRoutes.examples.value,
    page=example_page
))


my_app_layout = Layout(
    top= [nav_bar_header], 
    routes=router.routes,  
    bottom=[footer] 
)


# sync layout component lifecycle methods
router.layout = my_app_layout

# handle when user enter url with path different than "/"
router.history.current = HistoryNode(home_page)
event_loop.run_until_complete(router.navigate(window.location.pathname))
