import pygame

class Game():
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.states = states
        self.state_name = start_state
        slef.state = self.states[self.state_name]
    
    def event_loop(self):
        for event in pygame.event.get():
            self.state.get_event(event)
    
    def flip_state(self):
        current_state = self.state_name
        next_state = self.state.next_state
        slef.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)