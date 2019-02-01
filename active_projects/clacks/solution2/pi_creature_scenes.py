from big_ol_pile_of_manim_imports import *


class OnAnsweringTwice(TeacherStudentsScene):
    def construct(self):
        question = TextMobject("Why $\\pi$?")
        question.move_to(self.screen)
        question.to_edge(UP)
        other_questions = VGroup(
            TextMobject("Frequency of collisions?"),
            TextMobject("Efficient simulation?"),
            TextMobject("Time until last collision?"),
        )
        for mob in other_questions:
            mob.move_to(self.hold_up_spot, DOWN)

        self.add(question)

        self.student_says(
            "But we already \\\\ solved it",
            bubble_kwargs={"direction": LEFT},
            target_mode="raise_left_hand",
            added_anims=[self.teacher.change, "thinking"]
        )
        self.change_student_modes("sassy", "angry")
        self.wait()
        self.play(
            RemovePiCreatureBubble(self.students[2]),
            self.get_student_changes("erm", "erm"),
            ApplyMethod(
                question.move_to, self.hold_up_spot, DOWN,
                path_arc=-90 * DEGREES,
            ),
            self.teacher.change, "raise_right_hand",
        )
        shown_questions = VGroup(question)
        for oq in other_questions:
            self.play(
                shown_questions.shift, 0.85 * UP,
                FadeInFromDown(oq),
                self.get_student_changes(
                    *["pondering"] * 3,
                    look_at_arg=oq
                )
            )
            shown_questions.add(oq)
        self.wait(3)


class AskAboutEqualMassMomentumTransfer(TeacherStudentsScene):
    def construct(self):
        pass


class ComplainAboutRelevanceOfAnalogy(TeacherStudentsScene):
    def construct(self):
        self.student_says(
            "Why would \\\\ you care",
            target_mode="maybe"
        )
        self.change_student_modes(
            "angry", "sassy", "maybe",
            added_anims=[self.teacher.change, "guilty"]
        )
        self.wait(2)
        self.play(
            self.teacher.change, "raise_right_hand",
            self.get_student_changes(
                "pondering", "erm", "pondering",
                look_at_arg=self.hold_up_spot,
            ),
            RemovePiCreatureBubble(self.students[2])
        )
        self.play(
            self.students[2].change, "thinking",
            self.hold_up_spot + UP,
        )
        self.wait(3)
