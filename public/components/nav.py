from .common import *
from zenaura.client.tags.builder import Builder

def NavItemText(href, text, class_names="", click=None):
  tag = Builder('a') \
    .with_attribute("class", class_names) \
    .with_attribute("href", href) \
    .with_text(text)
  if click:
    tag.with_attribute("py-click", click)
       
  return tag.build()

def NavItemIcon(href, img, class_names=""):
  return  Builder('a').with_attribute('href', href).with_attribute("class", class_names).with_child(img).build()

def SvgPath(linecap, linejoin, d):
        return  Builder('path') \
          .with_attribute('stroke-linecap', linecap) \
          .with_attribute('stroke-linejoin', linejoin) \
          .with_attribute('d', d) \
          .build()

def Svg(class_name, fill, viewBox, stroke, path, stroke_width=None):
        svg = Builder('svg') \
          .with_attribute('class', class_name) \
          .with_attributes(
                  fill=fill,
                  viewBox=viewBox,
                  stroke=stroke
          ).with_child(
                path
          )
        if stroke_width:
                svg.with_attribute('stroke-width', stroke_width)
        return svg.build()

def Span(class_name, text=None):
        span =  Builder('span').with_attribute('class', class_name)
        if text:
                span.with_text(text)
        return span.build()

def MenuSmallScreenBtn(show=False):
  xShow = "block" if show else "hidden"
  menuShow = "hidden" if show else "block"
  return ButtonWithAttrsChildren(
    class_name="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white",
    attrs={"type" : "button", "py-click": "nav_bar_header.toggle_mobile_menu"}, 
    children=[
      Span(class_name="absolute -inset-0.5"),
      Span(class_name="sr-only", text="Open main menu"),
      Svg(
        class_name=f"{menuShow} h-6 w-6", 
        fill="none", 
        viewBox="0 0 24 24", 
        stroke="currentColor", 
        path=SvgPath(
                linecap="round", 
                linejoin="round", 
                d='M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5'
        )
      ), 
      Svg(
        class_name=f"{xShow} h-6 w-6", 
        fill="none", 
        viewBox="0 0 24 24", 
        stroke="currentColor", 
        path=SvgPath(
                linecap="round", 
                linejoin="round", 
                d='M6 18L18 6M6 6l12 12'
        ),
        stroke_width="1.5"
      )
    ]
  )

def NavBarItems():
    return Div(
      "hidden sm:ml-6 sm:block",
      [
        Div(
          "flex space-x-4", 
          # add more nav items here
          [
            NavItemText(
                "javascript:;", 
                "Docs", 
                "rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white",
                "nav_bar_header.navigate_to_docs"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
            "nav_bar_header.navigate_to_components"
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
                "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
                "nav_bar_header.navigate_to_theme"

            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                "rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white",
                "nav_bar_header.navigate_to_examples"
            ),
          ]
        )
      ]
    )

def NavBarItemsMobile(show=False):
    btn_class ="block text-left px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white"
    visable = "" if show else "hidden"
    return Div(
      visable,
      [
        Div(
          "flex flex-col w-full space-y-1 px-2 pb-3 pt-2", 
          # add more nav items here
          [
            NavItemText(
                "javascript:;", 
                "Docs", 
                "block flex-auto w-screen text-left rounded-md bg-gray-900 px-3 py-2 text-base font-medium text-white"
            ),
            NavItemText(
            "javascript:;", 
            "Components", 
            btn_class,
            ),
            NavItemText(
                "javascript:;", 
                "Themes", 
              btn_class,
            ),
            NavItemText(
                "javascript:;", 
                "Examples", 
                btn_class
            ),
          ]
        )
      ]
    )

def NavBarLogo():
    return  Div(
    "flex flex-shrink-0 items-center",
        [
            Image("./public/logo.png", "Your Company", "32", "32", "h-8 w-auto")
        ]
    )

def NavBarRightContent():
    return Div(
    "absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0", 
      [
      
        ButtonWithAttrsChildren(
            "relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800",
            {"type": "button"},
            [
                Span("absolute -inset-1.5"),
                Span("sr-only", "View notifications"),
                Svg(
                    class_name="h-6 w-6", 
                    fill="none", 
                    viewBox="0 0 24 24", 
                    stroke="currentColor", 
                    path=SvgPath(
                            linecap="round", 
                            linejoin="round", 
                            d='M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0'
                    ),
                    stroke_width="1.5"
                )
            ]
        ),
        Div("relative ml-3", [
            Div("", [
                ButtonWithAttrsChildren(
                    "relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800",
                    {
                        "type": "button", 
                        'id' : 'user-menu-button',
                        'aria-expanded': 'false',
                        'aria-haspopup': 'true'
                    },
                    [
                        Span("absolute -inset-1.5"),
                        Span("sr-only", "Open user menu"),
                        Image(
                          "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
                          "", 
                          "32", 
                          "32", 
                          "h-8 w-8 rounded-full"
                        )
                    ]
                )
            ])
        ])
      ]
  )