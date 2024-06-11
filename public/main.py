from zenaura.client.app import Route, App
from zenaura.client.page import Page
from public.routes import ClientRoutes
from public.components.header import Header
from public.components.intro import IntroSection
from public.components.footer import Footer

import asyncio

# Instantiate components
nav_bar_header = Header()
intro_section = IntroSection()
footer = Footer()

# App and routing
router = App()
home_page = Page([nav_bar_header, intro_section, footer])

router.add_route(Route(
    title="Developer-Focused | Zenaura",
    path=ClientRoutes.home.value,
    page=home_page
))

# Run the application
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(router.handle_location())
