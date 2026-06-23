# -*- coding: utf-8 -*-
# Cross-cutting reading journeys (Map VII). Each is an Adlerian draft — a gateway
# to enter by, a handful of steps, and a synthesis the *reader* finishes. The
# links between consecutive steps are surfaced as "claims to verify", never as
# verdicts: the journey points at a relationship and asks you to test it.
#
# Every concept id below is validated against the live atlas at build time
# (merge.py raises if a journey references an id that no longer exists), so these
# stay honest as the dataset grows.
JOURNEYS = [
    {
        "title": "The Art of Letting Go",
        "blurb": "Four traditions on the same counsel — loosen your grip.",
        "gateway": {
            "id": "Stoic Apatheia",
            "framing": "Begin where the West learned to want less: the Stoic claim "
                       "that peace is freedom from being ruled by passion.",
        },
        "steps": [
            {"id": "Ataraxia",
             "why": "Epicurus reaches a neighbouring calm by a different road — "
                    "pleasure, rightly understood, as the absence of disturbance."},
            {"id": "Non-Attachment",
             "why": "The Gita turns the screw: act fully, but renounce any claim "
                    "on the fruit of the action."},
            {"id": "Wu Wei",
             "why": "Daoism stops striving altogether — the ease of moving with "
                    "the grain of things rather than against it."},
            {"id": "Anattā (No-Self)",
             "why": "The Buddhist limit case: perhaps there is no self left to "
                    "disturb in the first place."},
        ],
        "synthesis": "Four traditions counsel you to let go. Where do they actually "
                     "disagree — and is there anything you would refuse to release?",
    },
    {
        "title": "What Are You, Really?",
        "blurb": "The self, assembled and then taken apart.",
        "gateway": {
            "id": "Existential Self",
            "framing": "Start with the modern wager: you are not a fixed essence "
                       "but whatever you make of yourself.",
        },
        "steps": [
            {"id": "Condemned to be Free",
             "why": "If there is no given nature, freedom is not a gift but a "
                    "sentence you cannot escape."},
            {"id": "Relational Self",
             "why": "Confucius answers from the far end: you are the sum of your "
                    "relationships, not a solo project."},
            {"id": "Being-in-the-World",
             "why": "Heidegger dissolves the inner/outer line — you do not have a "
                    "world, you are your involvement in it."},
            {"id": "Anattā (No-Self)",
             "why": "And the Buddhist limit: look hard for the self and you find "
                    "only passing parts."},
        ],
        "synthesis": "Is there a 'you' underneath all the descriptions, or only the "
                     "descriptions? Write the version you would defend.",
    },
    {
        "title": "When the Sky Goes Silent",
        "blurb": "Meaning, after the old source of it is gone.",
        "gateway": {
            "id": "The Death of God",
            "framing": "Nietzsche's diagnosis: the old source of meaning is gone, "
                       "and we have not yet reckoned with it.",
        },
        "steps": [
            {"id": "The Absurd",
             "why": "Camus names the gap — a mind that craves meaning, a universe "
                    "that returns silence."},
            {"id": "Meaning Is Created",
             "why": "The existentialist reply: if none is given, meaning is "
                    "something you make, not something you find."},
            {"id": "Eternal Recurrence",
             "why": "Nietzsche's test: would you will this same life again, "
                    "endlessly? Live so the answer could be yes."},
        ],
        "synthesis": "If no meaning is handed down, is one you author for yourself "
                     "enough to live by? Make your case.",
    },
    {
        "title": "Why Should I Obey?",
        "blurb": "Where the right to rule you comes from.",
        "gateway": {
            "id": "Social Contract",
            "framing": "Start with the founding question of politics: where does "
                       "the right to rule over you come from?",
        },
        "steps": [
            {"id": "The General Will",
             "why": "Rousseau's daring answer — legitimate power is the people "
                    "willing their own common good."},
            {"id": "Government by Virtue",
             "why": "Confucius locates authority elsewhere: in the ruler's "
                    "character, not in any contract."},
            {"id": "Karma",
             "why": "An Indian frame where justice is not enforced from above but "
                    "woven into cause and consequence."},
        ],
        "synthesis": "What would make you obey a rule you never chose? Name the "
                     "condition — or say honestly that there isn't one.",
    },
    {
        "title": "The Good Life, Four Ways",
        "blurb": "Rival targets for a life that goes well.",
        "gateway": {
            "id": "Eudaimonia",
            "framing": "Begin with Aristotle's question: not pleasure or duty, but "
                       "a whole life that goes well.",
        },
        "steps": [
            {"id": "Stoic Virtue",
             "why": "The Stoics narrow it: the only real good is virtue — "
                    "everything else is indifferent."},
            {"id": "Epicurean Pleasure",
             "why": "Epicurus widens it again, but to a sober pleasure — the "
                    "absence of pain and fear."},
            {"id": "Ren & Li",
             "why": "Confucius roots the good life in relationship and ritual, "
                    "not the solitary soul."},
            {"id": "Four Noble Truths",
             "why": "The Buddha reframes the whole project around the ending of "
                    "suffering."},
        ],
        "synthesis": "Each names a different target for a life. Which is yours "
                     "today — and what would change your mind?",
    },
]
