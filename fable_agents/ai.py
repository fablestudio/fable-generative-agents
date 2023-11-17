class Agent:

    def __init__(self, guid, location):
        self.guid = guid
        self.location = location

    def persona(self):
        #return datastore.personas[self.guid]
        return None


Actions = [
    {
        'action': 'go_to',
        'description': "Go to a location in the world",
        'parameters': {
            'destination': '<str: persona_guid, item_guid, or location.name to go to>',
            'goal': '<str: goal of the movement>',
        },
    },
    {
        'action': 'converse_with',
        'description': "Walk to another character and talk to them",
        'parameters': {
            'persona_guid': '<str: guid of the persona to converse with. You cannot talk to yourself.>',
            'topic': '<str: topic of the conversation>',
            'context': '<str: lots of helpful details the conversation generator can use to generate a conversation.'
                       ' It only has access to the context and the topic you provide, so be very detailed.>',
            'goal': '<str: goal of the conversation>',
        },
    },
    {
        'action': 'wait',
        'description': "Wait for a period of time while observing the world",
        'parameters': {
            'duration': '<int: number of minutes to wait>',
            'goal': '<str: goal of the waiting>',
        },
    },
    {
        'action': 'reflect',
        'description': "Think about things in order to synthesize new ideas and specific plans",
        'parameters': {
            'focus': '<str: the focus of the reflection>',
            'result:': '<str: the new specific enlightenment after reflecting.>',
            'goal': '<str: goal of reflecting>',
        },
    },
    {
        'action': 'interact',
        'description': "Interact with an item in the world",
        'parameters': {
            'item_guid': 'str: The id of the item to interact with',
            'interaction': 'str: The name of the interaction from the list per item.',
            'goal': '<str: goal of interaction>',
        },
    },
    {
        'action': 'take_to',
        'description': "Take an item or npc to a location in the world",
        'parameters': {
            'guid': '<str: persona_guid, item_guid to take to a location>',
            'destination': '<str: persona_guid, item_guid, or location.name to take the item or npc to>',
            'goal': '<str: goal of the take_to>',
        },
    },
    # 'exchange': {
    #     'description': 'Exchange resources with another character, shop, or storage. If no counterparty is specified,'
    #                    'try to use the closest.',
    #     'parameters': {
    #         'give': '<array: list of resources to give in the form of [resource_guid, item_quantity]>',
    #         'receive': '<array: list of resources to give in the form of [resource_guid, item_quantity]',
    #         'goal': '<str: goal of the exchange>',
    #         'counterparty': '<str: (optional) guid of a specific persona, shop, or storage to exchange with>',
    #     },
    # }
]







