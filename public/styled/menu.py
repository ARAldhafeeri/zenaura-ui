from public.components.common import *

def MenuExample(open):
  return Menu(
            Button(
                  "relative z-10 flex items-center p-2 text-sm text-gray-600 bg-white border border-transparent rounded-md focus:border-blue-500 focus:ring-opacity-40 dark:focus:ring-opacity-40 focus:ring-blue-300 dark:focus:ring-blue-400 focus:ring dark:text-white dark:bg-gray-800 focus:outline-none",
                  "open",
                  "components.toggle_dropdown",
            ),
            [
            ButtonWithAttrsChildren(
                 with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
                [
                  Image(
                      "https://images.unsplash.com/photo-1523779917675-b6ed3a42a561?ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8d29tYW4lMjBibHVlfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=face&w=500&q=200",
                      "jane avatar", "35", "35",
                      "flex-shrink-0 object-cover mx-1 rounded-full w-9 h-9"
                  ),
                  Div("mx-1 ", [
                      Header1("Jane Doe", "text-sm font-semibold text-gray-700 dark:text-gray-200"),
                      Paragraph("janedoe@exampl.com", "text-sm text-gray-500 dark:text-gray-400")
                  ])
                ] 
            ),
            HR(),
            ButtonWithAttrsChildren(
               with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
              [
                Span("text-light-gray1 dark:text-dark-page1", "Settings")
              ] 
            ),
            HR(),
            ButtonWithAttrsChildren(
               with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
              [
                Span("text-light-gray1 dark:text-dark-page1", "Keyboard shortcuts")
              ] 
            ),
            HR(),
            ButtonWithAttrsChildren(
               with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
              [
                Span("text-light-gray1 dark:text-dark-page1", "Company profile")
              ] 
            ),
            ButtonWithAttrsChildren(
               with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
              [
                Span("text-light-gray1 dark:text-dark-page1", "Team")
              ] 
            ),
            ButtonWithAttrsChildren(
               with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
              [
                Span("text-light-gray1 dark:text-dark-page1", "Invite colleagues")
              ] 
            ),
            HR(),
            ButtonWithAttrsChildren(
               with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
              [
                Span("text-light-gray1 dark:text-dark-page1", "Help")
              ] 
            ),
            HR(),
            ButtonWithAttrsChildren(
               with_theme_colors("flex hover:bg-light-hover dark:hover:bg-dark-hover overflow-auto w-full  items-center  items-center p-2 mt-2 text-sm"), {},
              [
                Span( "text-light-gray1 dark:text-dark-page1", "Sign Out")
              ] 
            ),
          ],
          open
        )