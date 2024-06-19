from zenaura.client.tags.builder import Builder
from zenaura.client.tags.node import Attribute

def Image(src, alt, width, height, classname=""):
		return Builder("img").with_attributes(
				src=src,
				alt=alt,
				width=width,
				height=height,
		).with_attribute("class", classname).build()

def Header2(text):
		return Builder('h2').with_text(text).build()

def Header1(text, class_names):
		return Builder('h1').with_text(text).with_attribute("class", class_names).build()

def Section(children, class_name="intro"):
		section = Builder('section').with_attribute('class', class_name).build()
		section.children = children
		return section

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

def ExpandableContent(code, is_visible, class_name=''):
		style = 'display: none;' if not is_visible else 'display: block;'
		content = Div('expandable-content', [
				Div('code-section ', [
						CodeBlock(code)
				])
		])
		content.attributes.append(Attribute('style', style))
		content.attributes.append(Attribute('class', class_name))
		content.attributes.append(Attribute('active', is_visible))
		return content

def Loader():
	return Div("loader self-center bg-light-white dark:bg-dark-gray1", [
		Div("", [
			Div("", [
			])
		])
	])