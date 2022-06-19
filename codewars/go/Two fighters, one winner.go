package main

import "fmt"

type Fighter struct {
	Name            string
	Health          int
	DamagePerAttack int
}

func (fighter Fighter) isDead() bool {
	return fighter.Health <= 0
}

func (fighter Fighter) Attack(enemy *Fighter) {
	enemy.Health -= fighter.DamagePerAttack
}

func DeclareWinner(fighter1 Fighter, fighter2 Fighter, firstAttacker string) string {
	nowAttack := firstAttacker
	for fighter1.isDead() == false && fighter2.isDead() == false {
		if fighter1.Name == nowAttack {
			fighter1.Attack(&fighter2)
			nowAttack = fighter2.Name
		} else {
			fighter2.Attack(&fighter1)
			nowAttack = fighter1.Name
		}
	}

	if fighter1.isDead() {
		return fighter2.Name
	}

	return fighter1.Name
}

func main() {
	fmt.Println(DeclareWinner(Fighter{"Lew", 10, 2}, Fighter{"Harry", 5, 4}, "Lew"))
	fmt.Println(DeclareWinner(Fighter{"Lew", 10, 2}, Fighter{"Harry", 5, 4}, "Harry"))
	fmt.Println(DeclareWinner(Fighter{"Harald", 20, 5}, Fighter{"Harry", 5, 4}, "Harry"))
	fmt.Println(DeclareWinner(Fighter{"Harald", 20, 5}, Fighter{"Harry", 5, 4}, "Harald"))
	fmt.Println(DeclareWinner(Fighter{"Jerry", 30, 3}, Fighter{"Harald", 20, 5}, "Jerry"))
	fmt.Println(DeclareWinner(Fighter{"Jerry", 30, 3}, Fighter{"Harald", 20, 5}, "Harald"))
}
