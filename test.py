from github import Github

# or using an access token
g = Github("f5fde9fde7194dfdc338f79310442c258b3ddca4")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)


