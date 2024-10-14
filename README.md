<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Matchmaker</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Project Matchmaker</h1>
    <form action="/find_projects" method="post">
        <label for="interests">Your Interests (comma-separated):</label>
        <input type="text" id="interests" name="interests" required>
        <button type="submit">Find Projects</button>
    </form>
</body>
</html>
