import os
import uuid
import xml.etree.ElementTree as ET

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