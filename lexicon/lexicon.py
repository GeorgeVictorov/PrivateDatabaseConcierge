MESSAGES: dict[str, str] = {
    '/start': '<b>Welcome to private database concierge!</b>\n\n'
              'Press /dql to enter DQL mode.\n'
              'Press /dml to enter DML mode.',
    '/dql': '<b>You are in DQL mode.</b>\n\n'
            'Enter your <i>SQL SELECT query</i>.\n\n'
            'To return, press the button below.',
    '/dml': '<b>You are in DML mode.</b>\n\n'
            'Enter your <i>SQL DML query</i> (insert, update, delete).\n\n'
            'To return, press the button below.'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'I hear the drums echoing tonight.',
    '/dql': 'The same old cars, same old streets.',
    '/dml': 'I\'ve watched you change.',
    '/cancel': 'Abandon ship.'
}

INFO: dict[str, str] = {
    'action': '<b>Choose an action:</b>',
    'no_data': '<b>No data found for the provided query.</b>',
    'abandon': '<b>Stop all the clocks, cut off the telephone.</b>',
    'csv_text': '<b>CSV file with selected data:</b>',
    'no_change': '<b>Failed to change data.</b>'
}
