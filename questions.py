
project_title = {
    "type": "input",
    "message": "Project Title:",
    "title": "title"
}

project_description = {
    "type": "input",
    "message": "Project Description",
    "description": "description"

}
project_license = {
    "type": "list",
    "message": "Pick A License:",
    "choices": ["MIT"],
},

confirmation = {
    "type": "confirm",
    "message": "Confirm?"
}

questions = [project_title, project_description, project_license, confirmation]
