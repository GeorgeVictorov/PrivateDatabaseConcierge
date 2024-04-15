MESSAGES: dict[str, str] = {
    '/start': '<b>Welcome to private database concierge!</b>\n\n'
              'Press /dql to enter DQL mode.\n'
              'Press /dml to enter DML mode.',
    '/dql': '<b>You are now in DQL mode.</b>\n\n'
            'Enter your <i>SQL SELECT query</i>, use double quotes if needed.',
    '/dml': '<b>You are now in DML mode.</b>\n\n'
            'Enter your <i>SQL DML query</i> (insert, update, delete), use double quotes if needed.'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'I hear the drums echoing tonight.',
    '/dql': 'The same old cars, same old streets.',
    '/dml': 'I\'ve watched you change.',
    '/cancel': 'Abandon ship.'
}
