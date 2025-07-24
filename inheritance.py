'''                                                         Inheritance in OOPs '''
# single level inheritance
# multi-level inheritance
# multiple inheritance
# hyrarchical inheritance
# hybrid inheritance

                                                                                # single level inheritance


# class Parent:
#     def parent_feature(self):
#         print("parent feature")

# class Child(Parent):
#     def child_features(self):
#         print("child features")

# p1 = Parent()
# p1.parent_feature()
# c1 = Child()
# c1.child_features()
# c1.parent_feature()



                                                                                 # multilevel inheritance


# class Gparents:
#     def gparent_feature(self):
#         print("gparent features")
# class Parent(Gparents):
#     def parent_features(self):
#         print("parent features")
# class Child(Parent):
#     def child_features(self):
#         print("child features")

# c1 = Child()
# c1.gparent_feature()
# c1.parent_features()
# c1.child_features()





                                                                               # multiple inheritance


# class Mother:
#     def mother_feature(self):
#         print("mother features")
# class Father:
#     def father_features(self):
#         print("father features")
# class Child(Mother,Father):
#     def child_features(self):
#         print("child features")


# c1 = Child()
# c1.father_features()
# c1.mother_feature()
# c1.child_features()


                                                                          # hyrarchical inheritance

# class Parent:
#     def parent_feature(self):
#         print("parent features")
# class Child1(Parent):
#     def Child1_features(self):
#         print("child1 features")
# class Child2(Parent):
#     def child2_features(self):
#         print("child2 features")

# c1 = Child1()
# c2 = Child2()
# c1.parent_feature()
# c2.parent_feature()

                                                     # hybrid inheritance - combination of all types