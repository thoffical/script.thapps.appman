import xbmc
import xbmcgui
import os

def get_installed_addons():
    """Retrieve the list of installed addons and their IDs."""
    addon_ids = []
    addon_path = xbmc.translatePath('special://home/addons/')
    
    # List all directories in the addons folder
    try:
        for addon in os.listdir(addon_path):
            if os.path.isdir(os.path.join(addon_path, addon)):
                addon_ids.append(addon)
    except Exception as e:
        xbmcgui.Dialog().ok("Error", f"Failed to retrieve addons: {str(e)}")
    
    return addon_ids

def uninstall_addon(addon_id):
    """Uninstall the addon using Kodi's built-in methods."""
    try:
        xbmc.executebuiltin(f"UninstallAddon({addon_id})")
        return True
    except Exception as e:
        xbmcgui.Dialog().ok("Error", f"Failed to uninstall {addon_id}: {str(e)}")
        return False

def main():
    """Main function to run the addon uninstallation process."""
    # Display a disclaimer to the user
    dialog = xbmcgui.Dialog()
    dialog.ok("Disclaimer", "By using this addon, the developer is not responsible for any harm to your device.")
    
    addon_ids = get_installed_addons()
    
    if not addon_ids:
        dialog.ok("No Addons", "No addons found to uninstall.")
        return
    
    # Show a list of installed addon IDs
    selected_addon = dialog.select("Select an addon to uninstall", addon_ids)
    
    if selected_addon >= 0:
        addon_id = addon_ids[selected_addon]
        confirm = dialog.yesno("Confirm Uninstall", f"Are you sure you want to uninstall {addon_id}?")
        
        if confirm:
            if uninstall_addon(addon_id):
                dialog.ok("Uninstall Complete", f"{addon_id} has been uninstalled.")
            else:
                dialog.ok("Uninstall Failed", f"Could not uninstall {addon_id}.")

if __name__ == "__main__":
    main()
