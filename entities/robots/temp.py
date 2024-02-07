import os
for robo in next(os.walk("."))[1]:
        if f"yaml" in next(os.walk(robo))[1]:
                continue
        os.makedirs(os.path.join(robo, "yaml"))
        os.rename(os.path.join(robo, f"{robo}.model.yaml"), os.path.join(robo, "yaml", f"{robo}.yaml"))
        os.symlink(
                os.path.join("yaml", f"{robo}.yaml"),
                os.path.join(".", robo, f"{robo}.model.yaml"),
        )
