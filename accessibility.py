import os
import xml.etree.ElementTree as ET
from lxml import etree
from lxml.etree import QName
    
def add_accessibility_identifier(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Determine platform type (iOS or macOS)
    platform_type = root.get('targetRuntime')

    # Find the customClass of the viewController
    custom_class = None
    for vc in root.findall(".//viewController"):
        custom_class = vc.get('customClass')
        if custom_class:
            break

    # Mapping of destination IDs to outlet properties
    outlet_properties = {}

    # Search for connections and map destinations to properties
    for connection in root.findall(".//connections/outlet"):
        destination = connection.get('destination')
        property_name = connection.get('property')
        if custom_class:
            property_name = f"{custom_class}_{property_name}"
        outlet_properties[destination] = property_name

    if platform_type == "iOS.CocoaTouch":
        # iOS logic
        for subview in root.findall(".//subviews/*"):
            subview_id = subview.get('id')
            if subview_id in outlet_properties:
                accessibility = subview.find('accessibility')
                if accessibility is None:
                    accessibility = ET.SubElement(subview, 'accessibility', key="accessibilityConfiguration")
                accessibility.set('identifier', outlet_properties[subview_id])
    elif platform_type == "MacOSX.Cocoa":
        # macOS logic
        def update_accessibility(view, view_id):
            if view_id in outlet_properties:
                accessibility = view.find('.//accessibility')
                if accessibility is None:
                    accessibility = ET.SubElement(view, 'accessibility')
                accessibility.set('identifier', outlet_properties[view_id])

        for view in root.findall(".//subviews/*"):
            view_id = view.get('id')
            update_accessibility(view, view_id)

    # Save the modified XML back to the file
    tree.write(xml_path)


def add_automation_id_to_wpf_lxml(xml_path):
    # Define and register namespaces
    nsmap = {
        'x': "http://schemas.microsoft.com/winfx/2006/xaml",
        'd': "http://schemas.microsoft.com/expression/blend/2008",
        'mc': "http://schemas.openxmlformats.org/markup-compatibility/2006",
        'Controls': "clr-namespace:MahApps.Metro.Controls;assembly=MahApps.Metro",
        'cal': "http://www.caliburnproject.org",
    }

    # Elements to add AutomationProperties.AutomationId
    elements_to_add_id = [
        'Button', 'TextBox', 'ComboBox', 'ListBox', 'RadioButton', 'CheckBox',
        'MenuItem', 'TabControl', 'ListView', 'TreeView', 'DataGrid', 'Expander',
        'ScrollViewer', 'Slider', 'ProgressBar', 'GroupBox', 'Label', 'Hyperlink',
        'Image', 'WebBrowser', 'Calendar', 'DatePicker', 'TimePicker', 'PasswordBox',
        'RichTextBox', 'DocumentViewer', 'MediaElement', 'UserControl', 'ContentControl',
        'Border'
    ]

    # Parse the XML file
    tree = etree.parse(xml_path)
    root = tree.getroot()

    # Extract x:Class attribute value
    x_class_attr = '{http://schemas.microsoft.com/winfx/2006/xaml}Class'
    x_class_value = ""
    if x_class_attr in root.attrib:
        x_class_value = root.attrib[x_class_attr].split('.')[-1]  # Optional: Extract the last part if it's a namespace


    # Initialize a counter for unique ID generation
    unique_id_counter = 1

    for elem in root.iter():
        elem_tag_name = etree.QName(elem).localname
        if elem_tag_name in elements_to_add_id:
            name_attr = QName(nsmap['x'], "Name")
            automation_id_attr = QName("AutomationProperties.AutomationId")

            if name_attr in elem.attrib:
                # Element has x:Name, use it for AutomationProperties.AutomationId
                name = elem.attrib[name_attr]
                elem.set(automation_id_attr, f"{x_class_value}_{name}")
            else:
                # Element doesn't have x:Name, generate a unique AutomationProperties.AutomationId
                unique_automation_id = f"{x_class_value}_{elem_tag_name}_{unique_id_counter}"
                elem.set(automation_id_attr, unique_automation_id)
                unique_id_counter += 1

    # Register the namespaces to ensure they are correctly used in the output
    for prefix, uri in nsmap.items():
        etree.register_namespace(prefix, uri)

    # Save the modified XML back to the file
    tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding="UTF-8", standalone=None)
