from public.components.common import *
# Define the required components

def TabButton(tab_number, label, active_tab_variable):
    class_expression = f"{{ 'bg-blue-600 text-white': {active_tab_variable} === {tab_number} }}"
    return ButtonWithAttrsChildren(
        class_name=f"flex-1 py-2 px-4 rounded-md focus:outline-none focus:shadow-outline-blue transition-all duration-300",
        attrs={"@click": f"{active_tab_variable} = {tab_number}", ":class": class_expression},
        children=[label]
    )

def TabContent(tab_number, active_tab_variable, header, content):
    style = 'display: none;' if f"{active_tab_variable} !== {tab_number}" else 'display: block;'
    return Div(
        class_name=f"transition-all duration-300 bg-white p-4 rounded-lg shadow-md border-l-4 border-blue-600",
        children=[
            Header2(header, "text-2xl font-semibold mb-2 text-blue-600"),
            Paragraph(content, "text-gray-700")
        ]
    )

# Main Tab Component

def TabsComponent(tab_buttons, tab_contents):
    return Div(
        class_name="bg-gray-100 font-sans flex items-center justify-center",
        children=[
            Div(
                class_name="p-8",
                children=[
                    Div(
                        class_name="max-w-md mx-auto",
                        children=[
                            Div(
                                class_name="mb-4 flex space-x-4 p-2 bg-white rounded-lg shadow-md",
                                children=tab_buttons
                            ),
                            *tab_contents
                        ]
                    )
                ]
            )
        ]
    )

