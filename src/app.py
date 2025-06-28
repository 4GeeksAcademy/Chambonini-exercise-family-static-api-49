from flask import Flask, jsonify, request
from flask_cors import CORS
from datastructures import FamilyStructure

app = Flask(__name__)
CORS(app)

jackson_family = FamilyStructure("Jackson")


@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"msg": "Member not found"}), 404


@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json()
    if not body:
        return jsonify({"msg": "No data provided"}), 400
    jackson_family.add_member(body)
    return jsonify({"msg": "Member added"}), 200


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200
