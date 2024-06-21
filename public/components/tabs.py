from public.components.common import *
from public.styles import with_theme_colors

def TabButton(tab_number, label, active_tab_variable, on_click, class_name, active_class=" me-2 inline-block p-5 border-b-2 border-light-green border-spacing-2 dark:border-dark-page1"):
    class_expression = active_class if tab_number == active_tab_variable else ""
    return ButtonWithAttrsChildren(
        class_name=class_name  + class_expression,
        attrs={
            "py-click": on_click,
            "name": tab_number
        },
        children=[label]
    )

def TabContent(tab_number, active_tab_variable, header, content):
    is_visible = "block" if tab_number == active_tab_variable else "hidden"
    return Div(
        class_name=f"{is_visible} transition-all duration-300 p-4 rounded-lg  border-l-4 ",
        children=[
            Header2(header, "text-2xl font-semibold mb-2 text-blue-600"),
            Paragraph(content, "text-gray-700")
        ]
    )

# Main Tab Component

def TabsComponent(tab_buttons, tab_contents):
  
	return Div(
		"bg-gray-100 font-sans",
		[
			Div(
				"p-8",
				[
					Div(
						"",
						[
							Div(
								"flex  border-b-2 border-light-green dark:border-dark-black",
								tab_buttons
							),
							Div(
								"mt-3", 
								[
									*tab_contents
								]
							)
						]
					)
				]
			)
		]
	)

