from dataclasses import dataclass

@dataclass
class empty_space:
          list_: list
empty_list=empty_space([])

class change_data:
          def normal_save(self,thing_to_save: list,save_on: empty_list.list_):
                    save_on.append(thing_to_save)
                    
          def tuple_save(self,thing_too_tup: list,save_tup_on_thing: empty_list.list_):
                    thing_too_tup=tuple(thing_too_tup)
                    save_tup_on_thing.append(thing_too_tup)
                    thing_too_tup=list(thing_too_tup)
                    
          def set_save(self,thing_to_list: list,save_list_on: empty_list.list_):
                    thing_to_list=set(thing_to_list)
                    save_list_on.append(thing_to_list)
                    thing_to_list=list(thing_to_list)

data_change=change_data()

