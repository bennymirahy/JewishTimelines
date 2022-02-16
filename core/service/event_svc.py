from core.models import Event


def save(devent):
    if 'id' in devent:
        event = Event.objects.get(pk=devent['id'])
        event.update_from_dict(devent)
    else:
        Event.objects.create(
            description=devent['description'],
            source=devent['source'],
            age=devent['age'],
            sourceAge=devent['sourceAge']
        )

def list_event():
    events = Event.objects.all()
    devents = [event.to_dict_json() for event in events]
    return devents

def remove(pk):
    Event.objects.get(pk=pk).delete()

def get(pk):
    event = Event.objects.get(pk=pk)
    devent = event.to_dict_json()
    return devent
