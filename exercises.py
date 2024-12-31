import random

push_exercise = [
    {
        "name": "barbell bench press",
        "equipment": ["barbell", "bench", "weight plates"]
    },
    {
        "name": "dumbbell bench press",
        "equipment": ["dumbbells, "bench"]
    },
    {
        "name": "incline barbell bench press",
        "equipment": ["barbell", "bench", "weight plates"]
    },
    {
        "name": "dumbbell barbell bench press",
        "equipment": ["dumbbells", "bench"]
    },
    {
        "name": "overheaad barbell press",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "overhead dumbell press",
        "equipment": ["dumbbells"]
    },
    {
        "name": "pushup",
        "equipment": ["none"]
    },
    {
        "name": "tricep pushdown",
        "equipment": ["cable machine"]
    },
    {
        "name": "barbell push press",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "dumbbell push press",
        "equipment": ["dumbbells"]
    },
    {
        "name": "barbell floor press",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "dumbbell floor press",
        "equipment": ["dumbbells"]
    }
]

pull_exercise = [
    {
        "name": "seated row",
        "equipment": ["cable machine"]
    },
    {
        "name": "lat pulldown",
        "equipment": ["cable machine"]
    },
    {
        "name": "bentover barbell row",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "bentover dumbell row",
        "equipment": ["dumbbells"]
    },
    {
        "name": "pull-uo",
        "equipment": ["none"]
    },
    {
        "name": "chin-up",
        "equipment": ["none"]
    },
    {
        "name": "bicep curl",
        "equipment": ["dumbbells"]
    },
    {
        "name": "face pull",
        "equipment": ["cable machine"]
    },
    {
        "name": "barbell upright row",
        "equipment": ["barbell", "weight plates"]
    },
    {
        "name": "dumbbell upright row",
        "equipment": ["dumbbells"]
    },


 "bicep curl", "face pull", "pendlay row", "upright row"]

squat_exercise = ["barbell back squat", "barbell front squat", "goblet squat", "jumping squat", "sumo squat", "overhead squat", "single leg squat", "box squat"]

lunge_exercise = ["forward lunge", "backward lunge", "curtsy lunge", "dumbbell stepup", "rearfoot elevated split squat", "front foot elevated split squat", "side lunge", "walking lunge"]

carry_exercise = ["farmers carry", "frontrack carry", "overhead carry", "suitcase carry", "goblet carry", "zercher carry"]

hinge_exercise = ["conventional deadlift", "romanian deadlift", "sumo deadlift", "single leg romanian deadlift", "good morning", "hip thrust"]


def workout_gen():
    push = random.choice(push_exercise)
    pull = random.choice(pull_exercise)
    squat = random.choice(squat_exercise)
    lunge = random.choice(lunge_exercise)
    carry = random.choice(carry_exercise)
    hinge = random.choice(hinge_exercise)
	
    workout = {
        "Push exercise": push,
        "Pull exercise": pull,
        "Squat exercise": squat,
        "Lunge exercise": lunge,
        "Carry exercise": carry,
        "Hinge exercise": hinge
    }

    return workout

if __name__ == "__main__":
    workout = workout_gen()
    print(workout)


