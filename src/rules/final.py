from rules.rules import Rules


class Final(Rules):
    def __str__(self):
        return '''# Default
FINAL,{proxy_group},dns-failed
'''.format(
            proxy_group=self.proxy_group
        )
