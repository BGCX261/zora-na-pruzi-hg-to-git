#!/usr/bin/env python3
# Copyright (c) 2012 Домоглед  <domogled@domogled.eu>
# @author Петр Болф <petr.bolf@domogled.eu>

'''
Hen je příkaz, koj vytvořží neo4j databázi
'''


from django.core.management.base import LabelCommand,  BaseCommand, CommandError
#from polls.models import Poll

class Command(LabelCommand):
    args = '<neo4j příkaz ...>'
    help = 'Administrace neo4j databáze'

    def handle(self, label,  *args, **options):
        self.stdout.write('Vytvořím neo4j databázi')
        self.stdout.write('label {}'.format(label) )
        self.stdout.write('\n'.join(args))
#        for poll_id in args:
#            try:
#                poll = Poll.objects.get(pk=int(poll_id))
#            except Poll.DoesNotExist:
#                raise CommandError('Poll "%s" does not exist' % poll_id)
#
#            poll.opened = False
#            poll.save()
#
#            self.stdout.write('Successfully closed poll "%s"' % poll_id)
