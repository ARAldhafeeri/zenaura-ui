from zenaura.client.tags.builder import Builder
from zenaura.client.tags.node import Attribute
from public.styles import with_theme_colors, btn_one_class, with_theme_colors_text_no_hover
from typing import List
# Base 
def Image(src, alt, width, height, classname=""):
		return Builder("img").with_attributes(
				src=src,
				alt=alt,
				width=width,
				height=height,
		).with_attribute("class", classname).build()

def Header2(text, class_name=""):
		return Builder('h2').with_attribute("class", class_name).with_text(text).build()

def Header1(text, class_names):
		return Builder('h1').with_text(text).with_attribute("class", class_names).build()

def Section(children, class_name="intro"):
		section = Builder('section').with_attribute('class', class_name).build()
		section.children = children
		return section

def HR():
	return Builder("hr").with_attribute('class', "w-full border-b-1 border-light-green dark:border-gray-700 ").build()

# features menu

def Paragraph(text, class_name=None):
		builder = Builder('p').with_text(text)
		if class_name:
				builder = builder.with_attribute('class', class_name)
		return builder.build()

def Div(class_name, children):
		div = Builder('div').with_attribute('class', class_name).build()
		div.children = children
		return div

def Button(class_name, text, onclick_handler=None, name=None):
		builder = Builder('button').with_attribute('class', class_name).with_text(text)
		if onclick_handler:
				builder = builder.with_attribute('py-click', onclick_handler)
		if name:
				builder = builder.with_attribute("name", name)
		return builder.build()

def ButtonWithAttrsChildren(class_name, attrs, children, onclick_handler=None, name=None):
		return Builder("button") \
			.with_attribute("class", class_name) \
			.with_attributes(**attrs).with_children(*children) \
			.with_attribute("py-click", onclick_handler) \
			.build()


def ExapandableContentButton(btn, content, is_visible):
		style = 'display: none;' if not is_visible else 'display: block;'
		active = "controlsActive" if is_visible else "controls"
		content = Paragraph(content, "featureParagraph")
		content.attributes.append(Attribute('style', style))
		content.attributes.append(Attribute("active", is_visible))
		return Div(active, [
				btn,
				content
				
		])

def CodeBlock(code):
		return Div("codeWrapper", [
				Builder('pre').with_child(Builder('code').with_attribute("class", "language-python").with_text(code).build()).build()
		])

def Tabs(tabs):
		return Div('tabs', [Button('tab-btn', tab) for tab in tabs])

def DocumentationButton():
		return Button('documentation-btn', 'Documentation')


def TableRow(content):
		return Div('row', [Div('cell', content)])

def Table(rows):
		return Div('table row', rows)

def ExpandableContent(code, class_name=''):
		content = Div('expandable-content', [
				Div('code-section ', [
						CodeBlock(code)
				])
		])
		content.attributes.append(Attribute('class', class_name))
		return content

def Loader():
	return Div("loader self-center bg-light-white dark:bg-dark-gray1", [
		Div("", [
			Div("", [
			])
		])
	])


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

def TabContent(tab_number, active_tab_variable, content):
    is_visible = "block" if tab_number == active_tab_variable else "hidden"
    return Div(
        f"{is_visible} transition-all duration-300 p-4",
        [
         content    
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

# nav 

def NavItemText(href, text, class_names, click=None):
	tag = Builder('a') \
		.with_attribute("class", class_names) \
		.with_attribute("href", href) \
		.with_text(text)
	if click:
		tag.with_attribute("py-click", click)
	return tag.build()

def NavItemTextNameFactory(href, text, class_names, click=None):
	tag = Builder('a') \
		.with_attribute("class", class_names) \
		.with_attribute("href", href) \
		.with_text(text)
	if click:
		tag.with_attribute("py-click", click)
	name = text.lower()
	tag.with_attribute("name", name)
	return tag.build()


def Link(href, text, class_names, target="_blank"):
	return Builder('a') \
    .with_attribute("class", class_names) \
    .with_attribute("href", href) \
		.with_attribute("target", target) \
    .with_text(text).build()
       
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

def MicroFrontend(url, class_names):
	return Builder("iframe").with_class(class_names).with_attributes(
		src=url,
		loading="lazy"
	).build()
