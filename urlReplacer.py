import os

# GLOBAL VARS
# path to walk (references path passed into Chronos container)
walk_path = '/www-css/themepark/CSS/'
# gilbn's URLS
old_css = 'https://gilbn.github.io/theme.park/'
old_resources = 'https://raw.githubusercontent.com/gilbN/theme.park/master/'
# local server URL
new = 'https://www.purplelan.xyz/themepark/'

# safely checks if a file has a string and replaces it with a different string
def string_replace(path, old_string, new_string):
    # need a place to store the contents of the CSS for the replcea to happen
    css = ''
    
    # read the CSS and see if themepark URL is in there
    with open(path) as f:
        css = f.read()
        if old_string not in css:
            print(f"[Matcher] \"{old_string}\" not found in {path}.")
            return

    # if the URL was found, open the file again for writing and replace the whole file with the fixed stuff
    with open(path, 'w') as f:
        print(f"[Replacer] Replacing \"{old_string}\" with \"{new_string}\" in {path}")
        s = css.replace(old_string, new_string)
        f.write(s)

# walks the path of themepark CSS and calls inplace_change on CSS files
def walk_tree():
    for root, dirs, files in os.walk(walk_path):
        for f in files:
            if f.endswith(".css"):
                full_path = os.path.join(root, f)
                
                # call for changes
                string_replace(full_path, old_css, new)
                string_replace(full_path, old_resources, new)

# start
if __name__ == '__main__':
    walk_tree()
