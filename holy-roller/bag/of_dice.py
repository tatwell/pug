# Your standard dice
four_sided_die = range(1,5)
six_sided_die = range(1,7)
ten_sided_die = range(1,11)
twenty_sided_die = range(1,21)

# And one truly evil one.
six_hundred_sixty_six_sided_die = range(1,667)

if __name__ == '__main__':
    import random

    print "Let's test some dice."

    for die in (four_sided_die, six_sided_die, ten_sided_die, twenty_sided_die,
                six_hundred_sixty_six_sided_die):
        results = []
        print "Testing %s-sided die" % (len(die))

        for n in range(100000):
            results.append(random.choice(die))

        assert len(set(die).symmetric_difference(set(results))) == 0, "This die seems off."

    print "These dice seem legit."
